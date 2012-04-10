#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import logging

class mylog(logging.getLoggerClass()):
    def __init__(self,label,fh=None, fmt=None, cnsl=None):
        logging.Logger.__init__(self,label)
        #self._logger = logging.getLogger(label)
        if fmt :
            formatter = fmt
        else :
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        try:
            if fh :
                self._fh = logging.FileHandler(fh)
                self._fh.setFormatter(formatter)
                self._fh.setLevel(logging.ERROR)
                self.addHandler(self_.fh)
        except :
            print("Can't open location %s" % fh)
        if cnsl :
            self._ch = logging.StreamHandler()
            self._ch.setLevel(logging.ERROR)
            self._ch.setFormatter(formatter)
            self.addHandler(self._ch)