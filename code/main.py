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
from pb import syncinfo_pb2         # SYNCINFO.BPB
from pb import training_session_pb2 # TSESS.BPB
from pb import user_database_pb2    # UDB.BPB
from pb import user_id_pb2          # USERID.BPB
from pb import user_physdata_pb2    # PHYSDATA.BPB


FILE_MAPPINGS = {
# 'ASAMPL.PP2' => Purpose?
  'ASAMPL0.BPB' : act_samples_pb2     .PbActivitySamples   (),
  'BASE.BPB'    : exercise_base_pb2   .PbExerciseBase      (),
  #'DEVICE.BPB'  : device_pb2          .PbDeviceInfo        (),  # BROKEN
  'DGOAL.BPB'   : act_dailygoal_pb2   .PbDailyActivityGoal (),
  'DSUM.BPB'    : dailysummary_pb2    .PbDailySummary      (),
  'ID.BPB'      : identification_pb2  .PbIdentifier        (),
  'PHYSDATA.BPB': user_physdata_pb2   .PbUserPhysData      (),
# 'PREFS.PBP'   ?
# 'PROFILE.PBP' ?
  'RECOVS.BPB'  : recovery_times_pb2  .PbRecoveryTimes     (),
  'SAMPLES.GZB' : exercise_samples_pb2.PbExerciseSamples   (),
  'SPORT.BPB'   : sport_pb2           .PbSport             (),
  'STATS.BPB'   : exercise_stats_pb2  .PbExerciseStatistics(),
  #'SYNCINFO.BPB': syncinfo_pb2        .PbSyncInfo          (),  # BROKEN
  'TSESS.BPB'   : training_session_pb2.PbTrainingSession   (),
  'USERID.BPB'  : user_id_pb2         .PbUserIdentifier    (),
  'UDB.BPB'     : user_database_pb2   .PbUserDb            (),
# 'UDEVSET.BPB' ?
  'ZONES.BPB'   : exercise_zones_pb2  .PbRecordedZones     (),
  }

  
# Logger setup
logging.basicConfig(format='%(asctime)-15s %(levelname)-8s %(message)s')
LOG = logging.getLogger()
# Set minimum level to DEBUG
LOG.setLevel(logging.DEBUG)


# Global sports lookup table
SPORTS = {}


def parse_ACT(path):
    """Parse activity files (ASAMPL0.BPB).
    
    Arguments:
    path -- ASAMPL0.BPB file path
    """
    with open(path, 'rb') as f:
        asamples = act_samples_pb2.PbActivityInfo()
        asamples.ParseFromString(f.read())
        
        print asamples
        print dir(asamples)
# end-of-function parse_ACT    


def parse_DSUM(path):
    """Parse daily summary files (DSUM.BPB).
    
    Arguments:
    path -- DSUM.BPB file path
    """
    with open(path, 'rb') as f:
        dsum = dailysummary_pb2.PbDailySummary()
        dsum.ParseFromString(f.read())
        
        print dsum
        print dir(dsum)
# end-of-function parse_DSUM    


def parse_E(path):
    pass
# end-of-function parse_E  


def parse_PHYSDATA(path):
    pass
# end-of-function parse_PHYSDATA    


def parse_SAMPLES(path):
    pass
# end-of-function parse_SAMPLES    


def parse_ID(path):
    """Parse identification files (ID.BPB).
    
    Arguments:
    path -- ID.BPB file path
    """
    with open(path, 'rb') as f:
        id = identification_pb2.PbIdentifier()
        id.ParseFromString(f.read())
        
        print id
        #print dir(id)
# end-of-function parse_ID    


def check_user_data(dir):
    LOG.debug('Parsing {}'.format(dir))

    dirs = list_dirs(dir)
        
    for d in dirs:
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


def check_file_exists(path):
    return os.path.exists(path) and os.path.isfile(path)
# end-of-function check_file_exists   


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Decode Polar A360 data tool.')
    parser.add_argument('--dump', required=True, help='Path to device dump (see: https://github.com/rsc-dev/loophole)')
    
    args = parser.parse_args()
    
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