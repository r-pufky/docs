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

    .. ports:: Files for Git
      :value0: /data/services/app.ini; Settings, and other stuff
      :value1: /data/services/git/git; Git repo location
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

  def _add_table_row(self, data, highlight):
    """Render RST for table row.

    Args:
      data: List of strings to render to table row.
      highlight: Boolean True to set background color to bg-light.
    """
    if highlight:
      bg = 'bg-light'
    else:
      bg = ''
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-md-6 p-0 m-0", self.c)
    self._rst.append("    :body: %s" % bg, self.c)
    self._rst.append("    %s" % repr(data[0])[1:-1], self.c)
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-sm-6 p-0 m-0", self.c)
    self._rst.append("    :body: %s" % bg, self.c)
    self._rst.append("    %s" % repr(data[1])[1:-1], self.c)

  def _add_dropdown_header(self):
    if 'generic' in self.options:
      self._rst.append(".. dropdown:: Files", self.c)
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

  def _add_table_headers(self):
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-md-6 p-0 m-0", self.c)
    self._rst.append("    :body: bg-light", self.c)
    self._rst.append("    Location", self.c)
    self._rst.append("    ---", self.c)
    self._rst.append("    :column: col-md-6 p-0 m-0", self.c)
    self._rst.append("    :body: bg-light", self.c)
    self._rst.append("    Purpose", self.c)

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
    self._add_table_headers()
    highlight = True
    for row in self._sanitize_data(20):
      highlight = not highlight
      self._add_table_row(row, highlight)
    self._add_update(self._sanitize_update())
    if 'ref' in self.options:
      for r in self._sanitize_ref():
        self._add_reference(r)

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('files', Files)
