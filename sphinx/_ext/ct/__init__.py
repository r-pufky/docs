# ct: Config Table sphinx extensions for documentation.
#
# See README.md or files for detailed documentation and config values.

import re
from . import config

from .v2 import cmdmenu
from .v2 import files
from .v2 import gpo
from .v2 import gui
from .v2 import ports
from .v2 import regedit
from .v2 import role

def setup(app):
  app.add_config_value('ct_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_separator_replace', config.DEFAULT_REPLACE, '')

  cmdmenu.setup(app)
  files.setup(app)
  gpo.setup(app)
  gui.setup(app)
  ports.setup(app)
  regedit.setup(app)
  role.setup(app)

  return {
    'version': '0.1',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
