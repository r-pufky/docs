# ct: Config Table sphinx extensions for documentation.
#
# See README.md or files for detailed documentation and config values.

import re
from . import cmdmenu
from . import config

from .windows import wfirewall
from .windows import wgpolicy
from .windows import wregedit
from .windows import wservice
from .windows import wtmanager
from .windows import wtschedule
from .windows import wsysprop

from .ubnt import uctree
from .ubnt import ufirewall
from .ubnt import ucontroller

def setup(app):
  app.add_config_value('ct_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_separator_replace', config.DEFAULT_REPLACE, '')
  cmdmenu.setup(app)

  wfirewall.setup(app)
  wgpolicy.setup(app)
  wregedit.setup(app)
  wservice.setup(app)
  wtmanager.setup(app)
  wtschedule.setup(app)
  wsysprop.setup(app)

  uctree.setup(app)
  ufirewall.setup(app)
  ucontroller.setup(app)

  return {
    'version': '0.1',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }