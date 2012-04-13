#! /usr/bin/env python
"""module docstring"""

# imports
import mylog
import logging
# constants
# exception classes
# interface functions
# classes
# internal functions & classes

class Server():
    def __init__(self,args):
        log = mylog.logg( 'vDeploy.%s' % __name__)
        log.warn("Starting daemon service")



def main():
    #    import doctest
    #    doctest.testmod()
    pass


if __name__ == '__main__':
    status = main()
    sys.exit(status)
# This is how a module should be structured.
# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
