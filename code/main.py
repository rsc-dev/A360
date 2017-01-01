#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.1'


import argparse
import gzip
import logging
import os
import re
import sys

from pb import act_dailygoal_pb2    # DGOAL.BPB
from pb import act_samples_pb2      # ASAMPL0.BPB 
from pb import exercise_base_pb2    # BASE.BPB
from pb import exercise_samples_pb2 # SAMPLES.GZB - GZIP
from pb import exercise_stats_pb2   # STATS.BPB
from pb import exercise_zones_pb2   # ZONES.BPB
from pb import dailysummary_pb2     # DSUM.BPB
from pb import identification_pb2   # ID.BPB
from pb import recovery_times_pb2   # RECOVS.BPB  
from pb import sport_pb2            # SPORT.BPB
from pb import sportprofile_pb2     # PROFILE.PBP
from pb import syncinfo_pb2         # SYNCINFO.BPB
from pb import training_session_pb2 # TSESS.BPB
from pb import user_database_pb2    # UDB.BPB
from pb import user_id_pb2          # USERID.BPB
from pb import user_physdata_pb2    # PHYSDATA.BPB
from pb import user_prefs_pb2       # PREFS.PBP
from pb import user_devset_pb2      # UDEVSET.BPB


# Global mappings for known files
FILE_MAPPINGS = {
  'ASAMPL0.BPB' : act_samples_pb2     .PbActivitySamples,
  'BASE.BPB'    : exercise_base_pb2   .PbExerciseBase,
  #'DEVICE.BPB'  : device_pb2          .PbDeviceInfo,           # BROKEN
  'DGOAL.BPB'   : act_dailygoal_pb2   .PbDailyActivityGoal,
  'DSUM.BPB'    : dailysummary_pb2    .PbDailySummary,
  'ID.BPB'      : identification_pb2  .PbIdentifier,
  'PHYSDATA.BPB': user_physdata_pb2   .PbUserPhysData,
  'PREFS.PBP'   : user_prefs_pb2      .PbGeneralPreferences,
  'PROFILE.PBP' : sportprofile_pb2    .PbSportProfile,
  'RECOVS.BPB'  : recovery_times_pb2  .PbRecoveryTimes,
  'SAMPLES.GZB' : exercise_samples_pb2.PbExerciseSamples,
  'SPORT.BPB'   : sport_pb2           .PbSport,
  'STATS.BPB'   : exercise_stats_pb2  .PbExerciseStatistics,
  #'SYNCINFO.BPB': syncinfo_pb2        .PbSyncInfo,             # BROKEN
  'TSESS.BPB'   : training_session_pb2.PbTrainingSession,
  'USERID.BPB'  : user_id_pb2         .PbUserIdentifier,
  'UDB.BPB'     : user_database_pb2   .PbUserDb,
  'UDEVSET.BPB' : user_devset_pb2     .PbUserDeviceSettings,
  'ZONES.BPB'   : exercise_zones_pb2  .PbRecordedZones,
  }

  
# Logger setup
logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(message)s')
LOG = logging.getLogger()
# Set minimum level to DEBUG
LOG.setLevel(logging.DEBUG)


# Global sports lookup table
SPORTS = {}


def get_parser(path):
    """Generic file parser based on file name.
    """
    LOG.debug('Looking for parser: {}'.format(path))
    parser = None
    
    if check_file_exists(path):
        file_name = os.path.basename(path)
        if file_name in FILE_MAPPINGS.keys():
            LOG.debug('Parser found.')
            # FILE_MAPPINGS holds class references for given files.
            # We get this reference and create instance of the class.
            parser = FILE_MAPPINGS[file_name]()
            
            if file_name is 'SAMPLES.GZB':
                with gzip.open(path) as g:
                    parser.ParseFromString(g.read())
            else:
                with open(path, 'rb') as f:
                    parser.ParseFromString(f.read())
        else:
            LOG.debug('Parser not found: {}'.format(path))
    else:
        LOG.error('File not found: {}'.format(path))
        raise IOError('File not found!')
    
    return parser
# end-of-function parse_file    


def parse_file(path):
    """Parse single file and print as json
    
    Arguments:
    path -- File to parse.
    """
    LOG.debug('Parsing single file {}'.format(dir))
    
    if check_file_exists(path):
        parser = get_parser(path)
        if parser is not None:
            print parser
    else:
        LOG.error('File not found: {}'.format(path))
        raise IOError('File not found!')
# end-of-function parse_file    


def check_user_data(dir):
    """Walk device dump and parse user data files.
    
    Arguments:
    dir -- Dump directory.
    """
    LOG.debug('Parsing {}'.format(dir))

    dirs = list_dirs(dir)
        
    for d in dirs:
        files = list_files(os.path.join(dir, d))
        
        for f in files:
            parser = get_parser(os.path.join(dir, d, f))
            if parser is not None:
                print parser
        
        subdirs = list_dirs(os.path.join(dir, d))
        # Filter only subdirs with date as name, i.e.: 20161213
        subdirs = filter(lambda x:re.match('\d{6}', x), subdirs)
        LOG.debug('Found dirs: {}'.format(str(subdirs)))
        
        for subd in subdirs:
            LOG.debug('Parsing {}'.format(subd))
            items = list_dirs(os.path.join(dir, d, subd))
            LOG.debug('Found dirs: {}'.format(str(items)))
            
            if 'ACT' in items:
                act_file = os.path.join(dir, d, subd, 'ACT', 'ASAMPL0.BPB')
                if check_file_exists(act_file):
                    pass
                    #parse_ACT(act_file)
                
                id_file = os.path.join(dir, d, subd, 'ACT', 'ID.BPB')
                if check_file_exists(id_file):
                    pass
                    #parse_ID(id_file)
                
            if 'DSUM' in items:
                dsum_file = os.path.join(dir, d, subd, 'DSUM', 'DSUM.BPB')    
                if check_file_exists(dsum_file):
                    pass
                    #parse_DSUM(dsum_file)
# end-of-function check_user_data


def build_sports_lookup(dir):
    """Parse given dir for subdirectories with SPORT.BPB files and 
    build global SPORTS table with parsed Sport structures.

    Arguments:
    dir -- Root dir for sports subdirectories.
    """
    for sport_id in os.listdir(dir):
        sport = sport_pb2.PbSport()
        
        p = os.path.join(dir, sport_id, 'SPORT.BPB')
        with open(p, 'rb') as f:
            sport.ParseFromString(f.read())
    
        SPORTS[int(sport_id)] = sport
    
    LOG.debug('Found {} sports descriptors.'.format(len(SPORTS)))
# end-of-function build_sports  


def list_dirs(dir):
    """
    Return list of all subdirectories for given root directory.
    
    Arguments:
    dir -- Root directory to parse.
    """
    dirs = [d for d in os.listdir(dir) if not os.path.isfile(os.path.join(dir, d))]
    return dirs
# end-of-function    


def list_files(dir):
    """
    Return list of all files for given directory.
    
    Arguments:
    dir -- Directory to parse.
    """
    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    return files
# end-of-function  


def check_file_exists(path):
    return os.path.exists(path) and os.path.isfile(path)
# end-of-function check_file_exists   


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Decode Polar A360 data tool.')
    
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument('--dump', help='Path to device dump (see: https://github.com/rsc-dev/loophole).')
    target.add_argument('--file', help='Decode single file.')
    
    parser.add_argument('--quiet', action='store_true', help='Turn off debug info.')
    
    args = parser.parse_args()
    
    if args.quiet:
        LOG.setLevel(logging.WARNING)
    
    if args.file is not None:
        parse_file(args.file)
    else:
        if os.path.isdir(args.dump):
            LOG.debug('Dump dir ({}) is OK.'.format(args.dump))
            
            # Build sports lookup table
            LOG.debug('Building sports table...')
            sports = os.path.join(args.dump, 'SYS', 'SPORT')
            build_sports_lookup(sports)
            
            # Parse device dump directory
            LOG.debug('Looking for user data...')
            user = os.path.join(args.dump, 'U')
            check_user_data(user)
            
            sys.exit(0)
        else:
            LOG.critical('Invalid dump dir ({}).'.format(args.dump))
            sys.exit(-1)
        
# end-of-function main


##
#  Entry point.
if __name__ == '__main__':
    main()