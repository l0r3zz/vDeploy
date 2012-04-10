#   Copyright (c) 2012 Geoffrey White
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#! /usr/bin/env python

"""
Module Doc String
"""

import argparse

LPORT_DEFAULT = 33777

def main():

    try: # catch ^C and exit

        parser = argparse.ArgumentParser(description="Deploy VMs into your cloud infrastructure")

        parser.add_argument("-u", "--user", default="root",
                          help=("Default user to provide for login"
                                 " to hypervisors default = %(default)s"))
        parser.add_argument("-p", "--password", default="password",
                          help=("Default password to provide for login"
                                 " to hypervisors default = %(default)s"))

        parser.add_argument("-D","--daemonize",action="store_true",
                            help=("Start %(prog)s as a daemon"))

        parser.add_argument("-P",'--lport',type=int,default=LPORT_DEFAULT,
                           help="listen on port default: %(default)s")

        args = parser.parse_args()


    except KeyboardInterrupt:
        print ""
        return(1)

if __name__ == "__main__":
    status = main()
    sys.exit(status)