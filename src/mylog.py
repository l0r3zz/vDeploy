#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

#! /usr/bin/env python

"""
Module DocString.
"""
import sys
import logging

class mylog(logging.getLoggerClass()):
    def __init__(self,label,fh=None, fmt=None, cnsl=None):
        logging.Logger.__init__(self,label)
        
        if fmt :
            formatter = fmt
        else :
            formatter = logging.Formatter(
                '%(asctime)s %(levelname)s\t:%(name)s [%(module)s:%(lineno)d] %(message)s')
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
