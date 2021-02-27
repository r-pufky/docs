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

    .. regedit:: Generic dropdown using ; as delims.
      :path:   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               CapabilityAccessManager\ConsentStore\microphone
      :value0: Value1; {SZ}; Allow
      :value1: Value2; {DWORD}; Allow
      :value2: Value3; {DELETE}; {DELETE}
      :ref:    https://some.reference.site,
               https://some.reference.site2
      :update: 2021-01-01
      :delim:  ;
      :generic:
      :open:

      Generic dropdown using ; as delims.

      .. warning::
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

  def _add_value_row(self, data):
    """Add RST row for :value: directive.

    Args:
      data: List of strings to render to row.
    """
    for x in data:
      self._rst.append("    ---", self.c)
      self._rst.append("    %s" % repr(x)[1:-1], self.c)

  def _add_dropdown_header(self):
    if 'generic' in self.options:
      self._rst.append(".. dropdown:: Registry", self.c)
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
    self._add_path(self._sanitize_path())
    for row in self._sanitize_data():
      self._add_value_row(row)
    self._add_update(self._sanitize_update())
    if 'ref' in self.options:
      for r in self._sanitize_ref():
        self._add_reference(r)

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('regedit', Regedit)
