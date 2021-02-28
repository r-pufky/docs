# ct: Config Table sphinx extensions for documentation.
#
# See README.md or files for detailed documentation and config values.

import re
from . import cmdmenu
from . import config

from .generic import ggui
from .generic import table

from .v2 import regedit
from .v2 import gpo
from .v2 import ports
from .v2 import files
from .v2 import gui

def setup(app):
  app.add_config_value('ct_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_separator_replace', config.DEFAULT_REPLACE, '')
  cmdmenu.setup(app)

  ggui.setup(app)
  table.setup(app)

  regedit.setup(app)
  gpo.setup(app)
  ports.setup(app)
  files.setup(app)
  gui.setup(app)

  return {
    'version': '0.1',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
