#! /usr/bin/env python
"""Virtual Infrastructure Descriptor Language"""

# imports
import yaml
# constants
# exception classes
# interface functions
def vidl(*args, **kwargs):
    loadstring = ''
    for file in args:
        loadstring.append(open(file).read())
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
