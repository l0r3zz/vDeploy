#! /usr/bin/env python
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.



"""
Mylog module
Subclasses standard python logging module and adds some convenience to it's use.
Like being able to set GMT timestamps
"""
import sys
import time
import logging

class mylog(logging.getLoggerClass()):
    def __init__(self, label, fh=None, llevel='WARN', fmt=None, gmt=False, cnsl=None, sh=None):
        r"""
        Constructor for logging module
        string:label     set the name of the logging provider
        string:fh        pathname of file to log to, default is no logging to a 
                         file
        string:llevel    string of the loglevel
        string:fmt       custom format string, default will use built-in
        bool:gmt         set to True to log in the machines vision of GMT time 
                         and reflect it in the logs
        bool:cnsl        set to True if you want to log to console
        int:sh           file descriptor for log stream defaults to sys.stderr

        returns:         a singleton object
        ************************* doctest *************************************
        # when invoking mylog() set sh=sys.stdout this is needed for doctest
        >>> t = mylog("test logger", cnsl=True, sh=sys.stdout) 
        >>> print t # doctest: +ELLIPSIS
        <...mylog object at 0x...>
        >>> t.warn("hello world!") #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        2... WARNING    :test logger [...] hello world!
        >>> t.error("should see this")#doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        2... ERROR    :test logger [...] should see this
        >>> t.info("should not see this")
        >>> t.debug("0x1337")  # or this
        >>> 
        ***********************************************************************
        """

        
        logging.Logger.__init__(self,label)

        n_level = getattr(logging, llevel.upper(), None)
        if not isinstance(n_level, int):
            raise ValueError('Invalid log level: %s' % llevel)

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

                self._fh = logging.FileHandler(fh)
                self._fh.setFormatter(formatter)
                self._fh.setLevel(n_level)
                self.addHandler(self._fh)
        except IOError :
            print("Can't open location %s" % fh)

        if cnsl :
            if sh :
                self._ch = logging.StreamHandler(sh)
            else:
                self._ch = logging.StreamHandler()
            self._ch.setLevel(n_level)
            self._ch.setFormatter(formatter)
            self.addHandler(self._ch)



def main():
    logger = mylog("Test Logger",llevel='DEBUG', cnsl=True,sh=sys.stdout)
    logger.info("Hello World")
    logger.warn("Danger Will Robinson")
    logger.error("Time to Die")
    logger.debug("0x1337")
#    import doctest
#    doctest.testmod()
#    return 0

if __name__ == "__main__" :
    main()
    sys.exit(0)
