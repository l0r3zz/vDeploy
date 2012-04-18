#!/usr/bin/python
# Simple program to pretty print JSON from a YAML definition

import simplejson
import yaml
import sys
try:
    config = yaml.load_all(file( sys.argv[1]))
    for c in config:
        simplejson.dump(c,sys.stdout,sort_keys=True, indent=4)

except IOError:
    print( "File %s not found" % sys.argv[1])
    sys.exit(1)
except IndexError:
    print("Usage  %s <filename>" % sys.argv[0])
    sys.exit(0)
sys.exit(0)
