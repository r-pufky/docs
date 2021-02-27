# gui config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles


class Gui(ct.AbstractConfigTable):
  """Generate GUI elements in a sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :path:         String GUI navigation path to window. Required.
    :nav:          String GUI navigation path to application.
    :label:        Alternative generic label, defualt 'GUI'.
    :value{0..35}: List of Option, Setting strings for GUI.
    :ref:          List of reference URI's.
    :update:       String datetime last time references/settings were checked.
    :delim:        Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:      Use generic 'GUI' dropdown label, in light-grey.
    :open:         Set to expand the dropdown by default.

  conf.py options:
    ct_gui_separator: Unicode separator to use for path. This uses the
        Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_gui_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.

  Examples:
    .. gui::   Radarr Importing
      :nav:    ⌘ --> chrome --> https://radarr
      :path:   Settings --> Media Management --> Importing
      :value0: Skip Free Space Check, No
      :value1: Use Hardlinks Instead of Copy, No
      :value2: Import Extra Files, No
      :update: 2021-01-01
      :open:

      Dropdown opened by default, using commas as delim.

      .. info::
        Additional rst can be used here.

    .. gui::   Radarr Importing
      :path:   Settings --> Media Management --> Importing
      :label:  Chrome
      :value0: Skip Free Space Check; No
      :value1: Use Hardlinks Instead of Copy; No
      :value2: Import Extra Files; No
      :update: 2021-01-01
      :delim:  ;
      :generic:
      :open:

      Generic GUI dropdown, using ; as delim and Chome as the label.

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
    'value31': directives.unchanged,
    'value32': directives.unchanged,
    'value33': directives.unchanged,
    'value34': directives.unchanged,
    'value35': directives.unchanged,
    'ref': directives.unchanged,
    'update': directives.unchanged,
    'delim': directives.unchanged,
    'open': directives.flag,
    'generic': directives.flag,
    'nav': directives.unchanged,
    'label': directives.unchanged,
  }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.sep = config.get_sep(
      self.state.document.settings.env.config.ct_gpo_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_gpo_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

  def _sanitize_version(self):
    """Returned sanitized List of supported versions."""
    if 'version' in self.options:
      return self._parse_list('version')
    return None

  def _add_value_row(self, data):
    """Add RST row for :value: directive.

    Args:
      data: List of strings to render to row.
    """
    for x in data:
      self._rst.append("    ---", self.c)
      self._rst.append("    :column: col-md-6", self.c)
      self._rst.append("    %s" % repr(x)[1:-1], self.c)

  def _add_dropdown_header(self):
    if 'generic' in self.options:
      if 'label' in self.options:
        self._rst.append(".. dropdown:: %s" % self.options['label'], self.c)
      else:
        self._rst.append(".. dropdown:: GUI", self.c)
      self._rst.append("  :title: font-weight-bold", self.c)
      self._rst.append("  :animate: fade-in", self.c)
    else:
      self._rst.append(".. dropdown:: %s" % self.title.astext(), self.c)
      self._rst.append("  :container: + shadow", self.c)
      self._rst.append("  :title: bg-primary text-white font-weight-bold", self.c)
      self._rst.append("  :animate: fade-in", self.c)

    if 'open' in self.options:
      self._rst.append("  :open:", self.c)

  def _add_panel_template(self):
    self._rst.append("", self.c)
    self._rst.append("  .. panels::", self.c)
    self._rst.append("    :container: container-lg pb-3", self.c)
    self._rst.append("    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-0 m-0", self.c)
    self._rst.append("    :card: border-0", self.c)
    self._rst.append("", self.c)
    self._rst.append("    :column: col-lg-12 p-0 m-0", self.c)
    for line in self.content:
      self._rst.append("    %s" % line, self.c)

  def _add_path(self, path):
    """Add RST row for :path: directive.

    Args:
      path: String to render to row.
    """
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-lg-12 p-0 m-0 font-weight-bold", self.c)
    self._rst.append("    :body: bg-light", self.c)
    # repr is used to auto-escape strings for rendering in sudo-rst (e.g. \\)
    # returns quoted, so strip quotes to ensure render correctly.
    self._rst.append("    %s" % repr(path)[1:-1], self.c)

  def _add_update(self, update):
    """Add RST row for :update: directive.

    Args:
      update: String update time to render to row.
    """
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-lg-12 p-0 m-0", self.c)
    self._rst.append("    :body: text-right", self.c)
    self._rst.append("    %s" % badges.update(update), self.c)

  def _add_version(self, version):
    """Add RST row for :version: directive.

    Args:
      version: String version to render to row.
    """
    self._rst.append('    %s' % self._convert_to_badge(version), self.c)

  def _add_reference(self, ref):
    """Add RST row for :ref: directive.

    Args:
      ref: String reference to render to row.
    """
    self._rst.append('    %s' % badges.ref(ref), self.c)

  def run(self):
    """Generated rendered rst.

    Data is processed to a in-memory rst list, then rendered directly to the
    current document.
    """
    self._add_dropdown_header()
    self._add_panel_template()
    self._add_nav_to_path()
    self._add_path(self.gen_label(self._sanitize_path()))
    for row in self._sanitize_data(35):
      self._add_value_row(row)
    self._add_update(self._sanitize_update())
    if 'version' in self.options:
      for v in self._sanitize_version():
        self._add_version(v)
    if 'ref' in self.options:
      for r in self._sanitize_ref():
        self._add_reference(r)

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_config_value('ct_gui_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_gui_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_directive('gui', Gui)
