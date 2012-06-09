#! /usr/bin/env python
"""Virtual Infrastructure Descriptor Language"""

# imports
import os
import yaml
import logging
import mylog
# constants
# exception classes
# interface functions
log = logging.getLogger('vDeploy.%s' % __name__)

def vidl(*args, **kwargs):
    """ args  - one or more file names containing descriptor code
        kwargs - a dict containing a mapping between descriptor filename
                extensions and actual paths to the definition files
                in the future this could be replaced with the preloaded
                context for the extension but this is easiest for now
    """
    loadstring = ''
    #now read the file definitions
    for file in args:
        ext = os.path.splitext(file)[1][1:] # get the extension without the dot
        # load the internal definitions for the file type
        loadstring += open(kwargs[ext]).read()
        # now load the file
        loadstring += open(file).read()
    return yaml.load(loadstring)
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
