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
    # Internal functions to main()
    def terminate(exitcode):
        log.error('program terminated prematurely... good bye')
        sys.exit(exitcode)
    # Main program code starts here
    try:
        # Gather and verify command line arguments 
        args = getopts.vdeploy_options()
        
        # Start Logging 
        log = mylog.logg('vDeploy',llevel=args.log,
                          lfile=args.logfile,cnsl=args.console)
        log.info('program start : %s' % args)
        
        # Load the Hypervisor, VM and Network Definition Files (YAML data structure templates)
        try:
            ddf_context = prov.DDFContext(args)
        except prov.DDFLoadError, err:
            log.error("Descriptor configuration file not found: %s" % err)
            print("Descriptor configuration file not found: %s" % err)
            terminate(1)

        # See if we are going to run as a service
        if args.daemonize :
            try:
                daemon_handle = vdeploy_server.Server(args,ddf_context)

            except vdeploy_server.DaemonError:
                log.warn("Could not start as a service, exiting")
                print ("Could not start as a service, exiting")
                terminate(1)
        else:
            pass


        log.info("program exiting normally")
        return(0)

    except getopts.ArgparseError, e:
        print ("Argument ERROR: %s" % e)
        sys.exit(1)  
    except KeyboardInterrupt:
        log.error("^C pressed")
        print ""
        terminate(1)


if __name__ == "__main__":
    status = main()
    sys.exit(status)
