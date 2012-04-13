#! /usr/bin/env python
"""
This module handles the gathering and validation of program arguments.
By validation we mean:
access to file system paths are verified.
ability to bind to ports are verified (if daemon mode is enabled)
argparse is used to get the command line arguments

"""

# imports
import os
import argparse
# constants
LPORT_DEFAULT = 33777
LOG_LEVELS = ['CRITICAL','ERROR','WARNING','WARN','INFO','DEBUG']
# exception classes
class ArgparseError(Exception):pass
# interface functions
def vdeploy_options():
        parser = argparse.ArgumentParser(description= 'Deploy VMs into your cloud infrastructure')

        parser.add_argument('-u', '--user', default='root',
                          help=("Default user to provide for login"
                                 " to hypervisors default = %(default)s"))
        parser.add_argument("-p", "--password", default="password",
                          help=("Default password to provide for login"
                                 " to hypervisors default = %(default)s"))

        parser.add_argument("-D","--daemonize",action="store_true",
                            help=("Start %(prog)s as a daemon"))

        parser.add_argument("-P",'--lport',type=int,default=LPORT_DEFAULT,
                           help="listen on port [default:%(default)s]")

        parser.add_argument('-l','--log',default='WARN',
                           help="set the log level [default:%(default)s]")

        parser.add_argument('--logfile',default='./vdeploy.log',
                           help="set the logfile path to: %(default)s")

        parser.add_argument("--console",action="store_true",
                            help=("Log to the console "))
        
        parser.add_argument('--ddf',default=None,
                           help="deployment description file")
        parser.add_argument('--rdf',default=None,
                           help="re-deployment description file")
        parser.add_argument('--hdf',default=None,
                           help="hypervisor description file")
        parser.add_argument('--ndf',default=None,
                           help="network description file")
        parser.add_argument('--vdf',default=None,
                           help="VM description file")
        parser.add_argument('--udf',default=None,
                           help="universal description file")
        
        args = parser.parse_args()
        # Validate as many of the arguments as possible
        if  args.lport < 0 or args.lport > 65536:
            raise ArgparseError("Listening port out of range")
        if args.log.upper() not in LOG_LEVELS:
            raise ArgparseError("Unspecified Log Level")
        
        file_check = True
        if args.ddf :
            if not os.path.exists(args.ddf):
                file_check = False
                print("%s : ddf file, no access" % args.ddf)        
        if args.rdf :
            if not os.path.exists(args.rdf):
                file_check = False
                print("%s : rdf file, no access" % args.rdf)
        if args.hdf :
            if not os.path.exists(args.hdf):
                file_check = False
                print("%s : hdf file, no access" % args.hdf)
        if args.ndf :
            if not os.path.exists(args.ndf):
                file_check = False
                print("%s : ndf file, no access" % args.ndf)
        if args.vdf :
            if not os.path.exists(args.vdf):
                file_check = False
                print("%s : vdf file, no access" % args.vdf)           
        if args.udf :
            if not os.path.exists(args.udf):
                file_check = False
                print("%s : udf file, no access" % args.udf)
        if not file_check :
            raise ArgparseError("description files are specified but missing")
          
        return args
# classes
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
