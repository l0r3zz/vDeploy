#! /usr/bin/env python
""" ESXI Hyperviosr and Virtual machine classes"""

# imports
import mylog
import logging
import pexpect
import pxssh
from hypervisor import *
from copy import deepcopy
# constants
# exception classes

# interface functions
log = logging.getLogger('vDeploy.%s' % __name__)

# classes

class Hyper_ESXi(Hypervisor):
    def __init__(self,hdf):
        # call the base class __init__
        super( Hyper_ESXi, self ).__init__(hdf)

    # The following Methods manipulate global state on the Hypervisor, these operations can
    # cause side effects that could effect current and future VMs that are running.

    def restart(self, *args, **kwargs):
        ''' restart/reboot or reset the Hypervisor, this operation is vendor specific
        '''
        raise HVUnimplemented("restart")

    def maintenance_enter(self, *args, **kwargs):
        ''' put the Hypervisor into maintenance mode (vmware), rescue mode (openstack)
        this operation is vendor specific, generally VMs are suspended, evacuated or
        powered off
        '''
        raise HVUnimplemented("maintenance_enter")

    def maintenance_exit(self, *args, **kwargs):
        ''' exit maintenance mode and restore the Hypervisor to normal operation
        this operation is vendor specific
        '''
        raise HVUnimplemented("maintenance_exit")

    def shutdown(self, *args, **kwargs):
        ''' shutdown the Hypervisor, requiring "manual" restart, this operation is 
        vendor specific
        '''
        raise HVUnimplemented("shutdown")

    def define_network(self, *args, **kwargs):
        ''' define logical networking on the hypervisor, this could include vswitches,
        and portgroups (vmware), bridges, taps, etc. this operation is vendor specific
        '''
        raise HVUnimplemented("define_network")

    def mount_object_store(self, *args, **kwargs):
        ''' binds an "object storwe" to a hypervisor for purposes of providing access to images
        for future vm_register and other vm related operations, this operation is vendor
        specific
        '''
        raise HVUnimplemented("mount_object_store")

    def register_vm(self, *args, **kwargs):
        ''' instantiate a runable VM from an image found on the mounted object store, make the
        VM runnable, but don't start it. This should return an object ref that can be used in
        the subsequent vm_xx calls.
        '''
        raise HVUnimplemented("register_vm")

    # The following methods perform VM related operations on the specific Hypervisor, only the
    # VM that it is applied to should be affected


    def vm_start(self, *args, **kwargs):
        raise HVUnimplemented("vm_start")

    def vm_stop(selfself,*args, **kwargs):
        raise HVUnimplementer("vm_stop")

    def vm_restart(self, *args, **kwargs):
        raise HVUnimplemented("vm_restart")

    def vm_suspend(self, *args, **kwargs):
        raise HVUnimplemented("vm_suspend")

    def vm_query_ip(selfself,*args, **kwargs):
        raise HVUnimplementer("vm_query_ip")

    def vm_destroy(selfself,*args, **kwargs):
        raise HVUnimplementer("vm_destroy")


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
