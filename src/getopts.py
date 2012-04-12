#! /usr/bin/env python
"""module docstring"""

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

        parser.add_argument('--logfile',default='./vdeploy.log',
                           help="set the logfile path to: %(default)s")

        parser.add_argument("--console",action="store_true",
                            help=("Log to the console "))

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
