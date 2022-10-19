# files config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles

class Files(ct.AbstractConfigTable):
  """Generate file listing elements in a sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :value{0..20}: List of File, Purpose strings for files.
    :ref:          List of reference URI's.
    :update:       String datetime last time references/settings were checked.
    :delim:        Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:      Use generic 'Files' dropdown label, in light-grey.
    :open:         Set to expand the dropdown by default.

  Examples:
    .. ports:: Files for Git
      :value0: /data/services/app.ini, Settings
      :value1: /data/services/git/git, Git repo location
      :ref:    https://some.reference.site,
               https://some.reference.site2
      :update: 2021-01-01
      :open:

      Dropdown opened by default, using commas as delim.

      .. info::
        Additional rst can be used here.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  has_content = True
  add_index = True
  option_spec = {
    'value0': directives.unchanged,
    'value1': directives.unchanged,
    'value2': directives.unchanged,
    'value3': directives.unchanged,
    'value4': directives.unchanged,
    'value5': directives.unchanged,
    'value6': directives.unchanged,
    'value7': directives.unchanged,
    'value8': directives.unchanged,
    'value9': directives.unchanged,
    'value10': directives.unchanged,
    'value11': directives.unchanged,
    'value12': directives.unchanged,
    'value13': directives.unchanged,
    'value14': directives.unchanged,
    'value15': directives.unchanged,
    'value16': directives.unchanged,
    'value17': directives.unchanged,
    'value18': directives.unchanged,
    'value19': directives.unchanged,
    'value20': directives.unchanged,
    'ref': directives.unchanged,
    'update': directives.unchanged,
    'delim': directives.unchanged,
    'open': directives.flag,
    'generic': directives.flag,
  }

  def run(self):
    """Generated rendered rst.

    Data is processed to a in-memory rst list, then rendered directly to the
    current document.
    """
    if 'generic' in self.options:
      self._dropdown('Files', icon='file-directory', color='light')
    else:
      self._dropdown(self.title.astext(), icon='file-directory')

    self._grid_item_card_horizontal_two_column_row(
        ['Location', 'Purpose'],
        bold=True,
        highlight=True)

    odd_row = False
    for row in self._sanitize_data(20):
      odd_row = not odd_row
      self._grid_item_card_horizontal_two_column_row(row, highlight=odd_row)

    self._grid_item_card_horizontal_content()
    self._grid_item_card_horizontal_update_footer(*self._generate_references())

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('files', Files)
