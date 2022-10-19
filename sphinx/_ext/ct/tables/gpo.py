# gpo config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles


class Gpo(ct.AbstractConfigTable):
  """Generate windows group policy elements in a sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :path:         String registry key path. Required.
    :value{0..30}: List of Option, Setting strings for policy.
    :ref:          List of reference URI's.
    :update:       String datetime last time references/settings were checked.
    :delim:        Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:      Use generic 'Registry' dropdown label, in light-grey.
    :open:         Set to expand the dropdown by default.

  conf.py options:
    ct_gpo_separator: Unicode separator to use for path. This uses the
        Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_gpo_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.

  Examples:
    .. gpo::    Enable logon logoff events policy policy
      :path:    Computer Configuration -->
                Windows Settings -->
                Security Settings -->
                Advanced Audit Policy Configuration -->
                System Audit Policies - Local Group Policy Object -->
                Logon/Logoff -->
                Audit Other Login/Logoff Events
      :value0:  ☑, Configure the following audit events
      :value1:  ☑, Success
      :value2:  ☑, Failure
      :update:  2021-01-01
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
    'value21': directives.unchanged,
    'value22': directives.unchanged,
    'value23': directives.unchanged,
    'value24': directives.unchanged,
    'value25': directives.unchanged,
    'value26': directives.unchanged,
    'value27': directives.unchanged,
    'value28': directives.unchanged,
    'value29': directives.unchanged,
    'value30': directives.unchanged,
    'ref': directives.unchanged,
    'update': directives.unchanged,
    'delim': directives.unchanged,
    'open': directives.flag,
    'generic': directives.flag,
  }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.sep = config.get_sep(
      self.state.document.settings.env.config.ct_gpo_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_gpo_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

  def run(self):
    """Generated rendered rst.

    Data is processed to a in-memory rst list, then rendered directly to the
    current document.
    """
    if 'generic' in self.options:
      self._dropdown('GPO', icon='note', color='light')
    else:
      self._dropdown(self.title.astext(), icon='note')

    self._grid_item_card_horizontal_container_path()
    for row in self._sanitize_data():
      self._grid_item_card_horizontal_two_column_row(row)
    self._grid_item_card_horizontal_content()
    self._grid_item_card_horizontal_update_footer(*self._generate_references())

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_config_value('ct_gpo_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_gpo_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_directive('gpo', Gpo)
