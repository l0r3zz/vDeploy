#! /usr/bin/env python
"""This module contains all code used to actually deploy VMs/networks
to varoius Hypervisors
"""

# imports
import os
import sys
import mylog
import logging
import yaml
import simplejson
import provisioning
import hypervisor

# constants
# exception classes
class DeployExecError(Exception): pass
# interface functions
log = logging.getLogger('vDeploy.%s' % __name__)
# classes
class Deploy:
    def __init__(self, ctx, args):
        log.info("Starting deployment Engine")
        # First, create some managed objects for the Hypervisors
        hvlist = []
        if not ctx.hdf:
            raise DeployExecError("No Hypervisors Provided")
        # The JSON representational datastructure is a bit ugly, but it needs to be
        # this way in order to facilitate the future implementation of ddf, rdf, and udf file formats.
        hvtemplate = ctx.hdf['HVDef'][0]['_Template_HVDef']
        for hv in ctx.hdf['HVDef'][1:]: # skip over the template dict
            try:
                hvobj = hypervisor.hypervisor_factory(hv)
                log.info("Created Hypervisor managed object %x:%s" %(id(hvobj),hv['Name']))
            except hypervisor.HVCreateError, err:
                log.warn("Error creating Hypervisor Managed Object %s" % err)
                hvobj = None
            hvlist.append(hvobj)
        ####  TESTING #####
        try:
            session = hvlist[0].ctl_session()
        except hypervisor.HVCtlchannelError:
            log.warn("Login to Hypervisor failed")
        else:
            print hvlist[0].sendcmd(session,'ls -l')
        # Now Create VM managed objects, bound to these Hypervisors
        vmlist = []
        if not ctx.vdf:
            raise DeployExecError("No VMs specified to deploy")

        vmtemplate = ctx.vdf['VMDef'][0]['_Template_VMDef']
        for vm in ctx.vdf['VMDef'][1:]: #skip over the template dict
            try:
                vmobj = hypervisor.vm_factory(vm,hvlist)
                log.info("Created VM managed object %x:%s" %(id(vmobj),vm['Name']))
            except hypervisor.VMCreateError, err:
                log.warn("Error creating VM Managed Object %s" % err)
                vmobj = None
            vmlist.append(vmobj)

        self.hvlist = hvlist
        self.vmlist = vmlist
        self.hvtemplate = hvtemplate
        self.vmtemplate = vmtemplate

        log.info("Ending deployment Engine")

    def status(self):
        return( "done")
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
