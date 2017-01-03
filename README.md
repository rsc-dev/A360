# A360 - Polar A360 data decoder

## About
Polar A360 data decoder tool. Beta.
Use [Loophole](https://github.com/rsc-dev/loophole) for memory dump.

Supported files:
* ASAMPL0.BPB
* BASE.BPB
* DGOAL.BPB
* DSUM.BPB
* ID.BPB
* PHYSDATA.BPB
* PREFS.PBP
* PROFILE.PBP
* RECOVS.BPB
* SAMPLES.GZB
* SPORT.BPB
* STATS.BPB
* TSESS.BPB
* USERID.BPB
* UDB.BPB
* UDEVSET.BPB
* ZONES.BPB

## Usage

```bash
c:\a360>python main.py -h
usage: main.py [-h] (--dump DUMP | --file FILE) [--quiet]

Decode Polar A360 data tool.

optional arguments:
  -h, --help   show this help message and exit
  --dump DUMP  Path to device dump (see: https://github.com/rsc-dev/loophole).
  --out OUT    Output file. If not set, console output is used.  
  --file FILE  Decode single file.
  --quiet      Turn off debug info.
```

Right now, only "--file: option works:

```bash
c:\a360>python main.py --quiet --file c:\a360\dump\U\0\20161124\DSUM\DSUM.BPB
date {
  year: 2016
  month: 11
  day: 24
}
steps: 2761
activity_calories: 108
training_calories: 262
bmr_calories: 1170
activity_goal_summary {
  activity_goal: 319.0
  achieved_activity: 314.645019531
  time_to_go_up {
    hours: 0
    minutes: 6
    seconds: 0
    millis: 0
  }
  time_to_go_walk {
    hours: 0
    minutes: 1
    seconds: 0
    millis: 0
  }
  time_to_go_jog {
    hours: 0
    minutes: 0
    seconds: 0
    millis: 0
  }
}
activity_class_times {
  time_non_wear {
    hours: 14
    minutes: 29
    seconds: 30
    millis: 0
  }
  time_sleep {
    hours: 6
    minutes: 42
    seconds: 30
    millis: 0
  }
  time_sedentary {
    hours: 0
    minutes: 41
    seconds: 30
    millis: 0
  }
  time_light_activity {
    hours: 0
    minutes: 54
    seconds: 30
    millis: 0
  }
  time_continuous_moderate {
    hours: 0
    minutes: 3
    seconds: 30
    millis: 0
  }
  time_intermittent_moderate {
    hours: 0
    minutes: 26
    seconds: 30
    millis: 0
  }
  time_continuous_vigorous {
    hours: 0
    minutes: 0
    seconds: 0
    millis: 0
  }
  time_intermittent_vigorous {
    hours: 0
    minutes: 42
    seconds: 0
    millis: 0
  }
}
activity_distance: 1865.51977539
```

### Dependencies
* [protobuf](https://pypi.python.org/pypi/protobuf/3.0.0b2) 

## License
Code is released under [MIT license](https://github.com/rsc-dev/a360/blob/master/LICENSE) © [Radoslaw '[rsc]' Matusiak](https://rm2084.blogspot.com/).