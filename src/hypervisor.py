#! /usr/bin/env python
"""Hyperviosr and Virtual machine classes"""

# imports
import mylog
import logging
import pexpect
import pxssh
from copy import deepcopy
# constants
# exception classes
class HVCreateError(Exception): pass
class VMCreateError(Exception): pass
class HVCtlchannelError(Exception): pass
class HVUnimplemented(Exception): pass

# interface functions
log = logging.getLogger('vDeploy.%s' % __name__)


def hypervisor_factory(hvdef):
    hvmo = Hypervisor(hvdef)
    log.info("hypervisor_factory")
    return hvmo

def vm_factory(vmdef,hvlist):
    return vmdef

# classes

class Hypervisor:
    def __init__(self,hdf):
        # Make a copy of the data from the descriptor
        self.hvdict = deepcopy(hdf)
        self.hvdict["session_list"] = []
        self.hvdict["vm_list"] = []

    def _consume_prompt(self,session):
        '''After you match a pattern in pexpect, you need to move the buffer
        ahead to be ready to match future input. Failure to do so will yield
        potentially incorrect results, including out of phase matching
        '''
        # consume the prompt (this is done a lot)
        session.expect([pexpect.TIMEOUT, "~ #"], timeout=2)

    def ctl_session(self,orig_prompt='[#$] '):
        ''' For Hypervisors that have CLI console that you can ssh into (most)
        Open up an ssh control session, that you can send VLI commands too
        '''
        self.orig_prompt = orig_prompt
        if len(self.hvdict["session_list"]) == self.hvdict["MaxCtlsessions"]:
            raise HVCtlchannelError("Maximum number of control sessions has been reached")
        # create a control tunnel to the Hypervisor
        user = self.hvdict["MgmtUser"]
        if not user:
            raise HVCtlchannelError("No admin user role specified")
        mgmtip = self.hvdict["MgmtIP"]
        if not mgmtip:
            raise HVCtlchannelError("No IP address specified")
        passwd = self.hvdict["MgmtPass"]
        if not passwd:
            raise HVCtlchannelError("No Password specified")

        ctnl = pxssh.pxssh()
        try:
            ctnl.login(mgmtip, user,
                               passwd, original_prompt=orig_prompt,
                               login_timeout=10,
                               auto_prompt_reset=False)
        except pexpect.EOF,e:
            raise HVCtlchannelError("Login to Hypervisor @ %s Timedout: %s" % (mgmtip,e))
        # Add the newly created session to the session list
        self.hvdict["session_list"].append(ctnl)
        return ctnl

    def sendcmd(self,chan,cmd,expect_string=None,timeout=3, op=None):
        self._consume_prompt(chan)
        op = op if op else self.orig_prompt
        expect_string = expect_string if expect_string else self.orig_prompt
        chan.sendline(cmd)
        retval = chan.expect([pexpect.TIMEOUT, op, expect_string], timeout=timeout)
        return (retval, chan.before, chan.after)

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
