#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#! /usr/bin/env python

"""
Mylog module
Subclasses standard python logging module and adds some convenience to it's use.
Like being able to set GMT timestamps
"""
import sys
import time
import logging

class mylog(logging.getLoggerClass()):
    def __init__(self,label,fh=None, fmt=None, gmt=True, cnsl=None):
        """
        Constructor for logging module
        string:label     set the name of the logging provider
        string:fh        pathname of file to log to, default is no logging to a file
        string:fmt       custom format string, default will use built-in
        bool:gmt         set to True to log in the machines vision of GMT time and reflect it in the logs
        bool:cnsl        set to True if you want to log to console
        
        This returns a singleton
        """
        logging.Logger.__init__(self,label)
        
        if fmt :
            formatter = fmt
        elif gmt :
            formatter = logging.Formatter(
                '%(asctime)s:Z %(levelname)s:%(name)s [%(module)s:%(lineno)d] %(message)s')
        else :
            formatter = logging.Formatter(
                '%(asctime)s %(levelname)s\t:%(name)s [%(module)s:%(lineno)d] %(message)s')     
        if gmt:
            logging.Formatter.converter = time.gmtime
            
        try:
            if fh :
                open(fh,'w').close()
                self._fh = logging.FileHandler(fh)
                self._fh.setFormatter(formatter)
                self._fh.setLevel(logging.WARN)
                self.addHandler(self._fh)
        except IOError :
            print("Can't open location %s" % fh)
            
        if cnsl :
            self._ch = logging.StreamHandler()
            self._ch.setLevel(logging.INFO)
            self._ch.setFormatter(formatter)
            self.addHandler(self._ch)
            
def main():
    logger = mylog("Test Logger", cnsl=True)
    logger.info("Hello World")
    logger.warn("Danger Will Robinson")
    logger.error("Time to Die")
    return 0

if __name__ == "__main__" :
    main()
    sys.exit(0)
