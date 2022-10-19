# ct: Config Table sphinx extensions for documentation.
#
# See README.md or files for detailed documentation and config values.

import re
from . import config

from .tables import cmdmenu
from .tables import files
from .tables import gpo
from .tables import gui
from .tables import ports
from .tables import regedit
from .tables import role

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
    'version': '1.0',
    'parallel_read_safe': True,
    'parallel_write_safe': True,
  }
