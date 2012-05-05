#! /usr/bin/env python
"""Hyperviosr and Virtual machine classes"""

# imports
# constants
# exception classes
class HVCreateError(Exception): pass
class VMCreateError(Exception): pass

# interface functions
def hypervisor_factory(hvdef):
    return hvdef

def vm_factory(vmdef,hvlist):
    return vmdef

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
