#! /usr/bin/env python
#   Copyright (c) 2012 Geoffrey White
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


"""
Module Doc String
"""
# imports

import sys
import getopts
import mylog
import prov
import vdeploy_server

# constants
# exception classes
# interface functions
# classes
# internal functions & classes

def main():

    try: # catch ^C and exit
        
        # Read the Command line Options
        args = getopts.vdeploy_options()
        
        # Start Logging 
        log = mylog.logg('vDeploy(main)',llevel=args.log,
                          fh=args.logfile,cnsl=args.console)

        log.info('program start : %s' % args)
        
        if args.daemonize :
            try:
                daemon_handle = vdeploy_server.Server(args)
            except:
                log.warn("Could not start as a service, exiting")
                terminate(1)
        log.info("program exiting normally")
        return(0)
        
    except KeyboardInterrupt:
        print ""
        return(1)

def terminate(exitcode):
    log.error('program terminated.. good bye')
    sys.exit(exitcode)


if __name__ == "__main__":
    status = main()
    sys.exit(status)
