#! /usr/bin/env python
"""This module contains all code used to actually deploy VMs/networks
to varoius Hypervisors
"""

# imports
import os
import sys
import mylog
import logging
import yaml
import simplejson
import provisioning
 
# constants
# exception classes
class DeployExecError(Exception): pass
# interface functions
# classes
class Deploy:
    def __init__(self, ctx, args):
        self.log = logging.getLogger('vDeploy.%s' % __name__)
        self.log.info("Starting deployment Engine")
        self.log.info("Ending deployment Engine")

    def status(self):
        return( "done")
# internal functions & classes

def main():
    #    import doctest
    #    doctest.testmod()
    pass


if __name__ == '__main__':
    status = main()
    sys.exit(status)
# This is how a module should be structured.
# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
