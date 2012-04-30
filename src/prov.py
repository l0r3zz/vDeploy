#! /usr/bin/env python
"""
This module reads the data from the definition files provided:
<file>.ddf          Deployment Definition File
                    A top level JSON specification of which VMs
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
                    A JSON specification of the the hypervisors
                    available for deployment. Information included
                    are things, like Hypervisor (vendor) type,
                    control IP addresses, NFS mount points
                    (for virtual disk transfers), etc
<file>.vdf          VM Definition File
                    A JSON specification, describing a VM template,
                    What Hypervisors it can be deployed on,
                    location of disk images, for each hypervisor,
                    provisioning limits (memsize, core maximums and
                    minimums, nic maximums and minimums, os type,
                    descriptions, etc.
<file>.ndf          A JSON specification, describing the available
                    logical network configurations available for
                    the deployment, this will include vswitches
                    on hypervisors, distributed vSwitches that span
                    hypervisors, and SDN logical networks. This 
                    definition might be mutually dependent on the 
                    hdf file.
<file>.udf          A JSON specification that combines the definitions of all of
                    the previous specifications (ddf, hdf, ndf,vdf). This can be
                    used for deployments that will always per performed to
                    a fixed infrastructure. As a testing or debugging tool,
                    or as a "job" that can be submitted to a vDeploy daemon.
                    
"""

# imports
import mylog
import logging

# constants
# exception classes
class DDFLoadError(Exception): pass

# interface functions
# classes
class DDFContext:
    def __init__(self,args):
        log = logging.getLogger('vDeploy.%s' % __name__)
        log.info("Starting Starting DDF file processing")
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
