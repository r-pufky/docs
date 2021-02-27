# sysdm config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles


class SysDM(ct.AbstractConfigTable):
  """Generate windows System Properties (sysdm.cpl) elements in sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :path:        String GUI navigation path. Required. Will pre-pend sysdm.cpl.
    :value{0..9}: List of Option, Setting strings for policy.
    :ref:         List of reference URI's.
    :version:     List of supported windows versions - see self._text_badges.
    :update:      String datetime last time references/settings were checked.
    :delim:       Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:     Use generic 'System Properties' dropdown label, in light-grey.
    :open:        Set to expand the dropdown by default.

  conf.py options:
    ct_sysdm_separator: Unicode separator to use for path. This uses the
        Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_sysdm_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.

  Examples:
    .. sysdm:: Add gpg to user system path
      :path:   Advanced -->
               Environment Variables -->
               User variables for {USER} -->
               Path -->
               Edit -->
               New
      :value0: Path, c:\Program Files (x86)\GnuPG\bin
      :update: 2021-02-19
      :version: {PRO}, {ENTERPRISE}, {EDU}
      :open:

      Dropdown opened by default.

    .. sysdm::  Add gpg to user system path
      :path:    Advanced -->
                Environment Variables -->
                User variables for {USER} -->
                Path -->
                Edit -->
                New
      :value0:  Path; c:\Program Files (x86)\GnuPG\bin
      :update:  2021-02-19
      :version: {PRO}, {ENTERPRISE}, {EDU}
      :generic:
      :delim:   ;
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
    'version': directives.unchanged,
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
      self._rst.append(".. dropdown:: GPO", self.c)
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
    self.options['path'] = '⌘ --> sysdm.cpl --> %s' % self.options['path']
    self._add_path(self.gen_label(self._sanitize_path()))
    for row in self._sanitize_data(30):
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
  app.add_config_value('ct_sysdm_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_sysdm_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_directive('sysdm', SysDM)
