# regedit config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles


class Regedit(ct.AbstractConfigTable):
  """Generate windows registry editor elements in a sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :path:        String registry key path. Required.
    :value{0..9}: List of Name, Type, Value strings for path.
    :ref:         List of reference URI's.
    :update:      String datetime last time references/settings were checked.
    :delim:       Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:     Use generic 'Registry' dropdown label, in light-grey.
    :open:        Set to expand the dropdown by default.

  Examples:
    .. regedit:: Dropdown opened by default, using commas as delim.
      :path:   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\microphone
      :value0: Value1, {SZ}, Allow
      :value1: Value2, {DWORD}, Allow
      :value2: Value3, {DELETE}, {DELETE}
      :ref:    https://some.reference.site,
               https://some.reference.site2
      :update: 2021-01-01
      :delim:  ,
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
    'path': directives.unchanged_required,
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
      self._dropdown('Regedit', icon='stack', color='light')
    else:
      self._dropdown(self.title.astext(), icon='stack')

    self._grid_item_card_horizontal_container_path()

    for row in self._sanitize_data():
      self._grid_item_card_horizontal_three_column_row(row)

    self._grid_item_card_horizontal_content()
    self._grid_item_card_horizontal_update_footer(*self._generate_references())

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('regedit', Regedit)
