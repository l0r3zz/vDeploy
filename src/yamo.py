#!/usr/bin/env python3
# Simple program to pretty print JSON from a YAML definition

import json
import yaml
import sys
try:
    config = yaml.safe_load(open(sys.argv[1]))
    json.dump(config, sys.stdout, sort_keys=True, indent=4)

except IOError:
    print( "File %s not found" % sys.argv[1])
    sys.exit(1)
except IndexError:
    print("Usage  %s <filename>" % sys.argv[0])
    sys.exit(0)
sys.exit(0)
