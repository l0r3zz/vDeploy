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
        sesson.expect([pexpect.TIMEOUT, "~ #"], timeout=30)

    def ctl_session(self):
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
        ctnl.login(mgmtip, user,
                           passwd, original_prompt='[#$] ',
                           login_timeout=60,
                           auto_prompt_reset=False)
        # Add the newly created session to the session list
        self.hvdict["session_list"].append(ctnl)
        return ctnl

    def restart(self, *args, **kwargs):
        pass

    def maintenance(self, *args, **kwargs):
        pass

    def shutdown(self, *args, **kwargs):
        pass

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
