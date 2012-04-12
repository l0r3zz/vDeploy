#! /usr/bin/env python
"""
This module handles the gathering and validation of program arguments.
By validation we mean:
access to file system paths are verified.
ability to bind to ports are verified (if daemon mode is enabled)
argparse is used to get the command line arguments

"""

# imports
import argparse
# constants
LPORT_DEFAULT = 33777
# exception classes
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

        parser.add_argument('--logfile',default=None,
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

        return parser.parse_args()
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
