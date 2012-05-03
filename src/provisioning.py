#! /usr/bin/env python
"""
This module reads the data from the definition files provided:
<file>.ddf          Deployment Definition File
                    A top level YAML specification of which VMs
                    should be applied to which Hypervisors and
                    wired to specific Virtual Networks, this
                    file relies on objects defined in the 
                    hdf (Hypervisor Definition File),
                    ndf (Network Definition File), and the
                    vdf (VM definition File)
                    each of these three files must have been 
                    read prior to the reading of the ddf,
                    in daemon mode, this file can be passed
                    via the incoming port, and the elements
                    are validated against the data base that has 
                    been pre-loaded with these files.
<file>.hdf          Hypervisor Definition File
                    A YAML specification of the the hypervisors
                    available for deployment. Information included
                    are things, like Hypervisor (vendor) type,
                    control IP addresses, NFS mount points
                    (for virtual disk transfers), etc
<file>.vdf          VM Definition File
                    A YAML specification, describing a VM template,
                    What Hypervisors it can be deployed on,
                    location of disk images, for each hypervisor,
                    provisioning limits (memsize, core maximums and
                    minimums, nic maximums and minimums, os type,
                    descriptions, etc.
<file>.ndf          A YAML specification, describing the available
                    logical network configurations available for
                    the deployment, this will include vswitches
                    on hypervisors, distributed vSwitches that span
                    hypervisors, and SDN logical networks. This 
                    definition might be mutually dependent on the 
                    hdf file.
<file>.udf          A YAML specification that combines the definitions of all of
                    the previous specifications (ddf, hdf, ndf,vdf). This can be
                    used for deployments that will always per performed to
                    a fixed infrastructure. As a testing or debugging tool,
                    or as a "job" that can be submitted to a vDeploy daemon.

It also reads in YAML template files that define the core data structures that the
above files use. 
hvdef.yaml          A YAML description of the basic structure used in the .hdf file
vmdef.yaml          A YAML description of the basic structure used to define a VM
netdef.yaml         A YAML description for virtual networks that attach the VMs

"""

# imports
import os
import sys
import mylog
import logging
import yaml
import simplejson

# constants
# search through this directory list to find the configuration files
CONFIG_DIR_DEFAULTS= ['/usr/local/share/vdeploy/','./.vdeploy/config/']

# names of the structure definition files, these are part of the program and
# only change from release to release 
HVDEF_TEMPLATE= 'hvdef.yaml'
VMDEF_TEMPLATE= 'vmdef.yaml'
NETDEF_TEMPLATE= 'netdef.yaml'

# exception classes
class DDFLoadError(Exception): pass
class DeployExecError(Exception): pass

# interface functions
# classes
class DDFContext:
    def __init__(self,args):
        self.log = logging.getLogger('vDeploy.%s' % __name__)
        self.log.info("Starting config file processing")

        # Scan for presence of config directory
        config_dir = './'
        for dpath in CONFIG_DIR_DEFAULTS:
            if os.path.exists(dpath):
                config_dir = dpath
                break

        # Attempt to load all of the data structure temple definitions
        try:
            hvpath = config_dir+HVDEF_TEMPLATE
            if os.path.exists(hvpath):
                self.hvtemplate =  yaml.load(file(hvpath))
                if not self.hvtemplate:
                    mylog.printlog(self.log,"%s is empty" % hvpath, 'INFO')
            else:
                raise DDFLoadError(hvpath)

            vmpath = config_dir+VMDEF_TEMPLATE
            if os.path.exists(vmpath):
                self.vmtemplate =  yaml.load(file(vmpath))
                if not self.vmtemplate:
                    mylog.printlog(self.log,"%s is empty" % vmpath, 'INFO')
            else:
                raise DDFLoadError(vmpath)

            netpath = config_dir+NETDEF_TEMPLATE
            if os.path.exists(netpath):
                self.nettemplate =  yaml.load(file(netpath))
                if not self.nettemplate:
                    mylog.printlog(self.log,"%s is empty" % netpath, 'INFO')
            else:
                raise DDFLoadError(netpath)

        except yaml.scanner.ScannerError,err:
            self.log.error("Error in YAML config file " % err)       

        self.log.info("Ending config file processing")

    def process_ddf_files(self,args):
        """
        This method takes a DDF context object which has been loaded with the context
        of what this current version is capable of, and create a deployment structure
        consisting of the definitions of what is available merged with the VM definitions.
        This context object can be passed off to the deployment engine for subsequent
        execution.
        """
        self.log.info("Starting DDF file processing")
        pass
        self.log.info("Ending DDF file processing")

class Deploy:
    def __init__(self, ctx, args):
        self.log = logging.getLogger('vDeploy.%s' % __name__)
        self.log.info("Starting deployment Engine")
        self.log.info("Ending deployment Engine")

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
