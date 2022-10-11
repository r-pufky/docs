# ansible role config table.

from .. import config
from .. import ct
from . import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles

class Role(ct.AbstractConfigTable):
  """Generate ansible role listing elements in a sphinx document.

  Badges ({KEYWORD}) are automatically converted using badges.badges.

  Directives:
    :galaxy:      String link to ansible galaxy repository.
    :source:      String link to ansible source repository.
    :service_doc: String link to role service docs (e.g. manuals).
    :ref:         List of reference URI's.
    :update:      String datetime last time references/settings were checked.
    :delim:       Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:     Use generic 'Files' dropdown label, in light-grey.
    :private:     Set to flag role as a non-exported role.
    :open:        Set to expand the dropdown by default.

  Examples:
    .. role:: radarr
      :galaxy:      https://galaxy.ansible.com/r_pufky/radarr
      :source:      https://github.com/r-pufky/ansible_radarr
      :service_doc: https://wiki.servarr.com/radarr
      :ref:    https://some.reference.site,
               https://some.reference.site2
      :update: 2021-01-01
      :open:

      Dropdown opened by default, using commas as delim.

      .. literalinclude:: ../README.md

      .. info::
        Additional rst can be used here.

    .. role:: radarr
      :galaxy:      https://galaxy.ansible.com/r_pufky/radarr
      :source:      https://github.com/r-pufky/ansible_radarr
      :service_doc: https://wiki.servarr.com/radarr
      :ref:    https://some.reference.site;
               https://some.reference.site2
      :update: 2021-01-01
      :delim:  ;
      :generic:
      :open:

      Generic dropdown using ; as delims.

      .. literalinclude:: ../README.md

      .. info::
        Additional rst can be used here.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  has_content = True
  add_index = True
  option_spec = {
    'galaxy': directives.unchanged,
    'source': directives.unchanged,
    'service_doc': directives.unchanged,
    'ref': directives.unchanged,
    'update': directives.unchanged,
    'delim': directives.unchanged,
    'private': directives.flag,
    'open': directives.flag,
    'generic': directives.flag,
  }

  def _add_dropdown_header(self):
    if 'generic' in self.options:
      self._rst.append(".. dropdown:: Ansible Role", self.c)
      self._rst.append("  :title: font-weight-bold", self.c)
      self._rst.append("  :animate: fade-in", self.c)
    else:
      self._rst.append(".. dropdown:: Ansible Role: %s" % self.title.astext(), self.c)
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
    self._rst.append("    Role Details: %s" % badges.update(update), self.c)

  def _add_reference(self, ref):
    """Add RST row for :ref: directive.

    Args:
      ref: String reference to render to row.
    """
    self._rst.append('    %s' % badges.ref(ref), self.c)

  def _add_named_link(self, option, text=None):
    """Add RST row for :ref: directive.

    Args:
      option: String directive option text to render badge link.
      text: String override option key with specific text for badge link.
    """
    if option in self.options:
      if text:
        self._rst.append('    %s' % badges.named(text, self.options[option]), self.c)
      else:
        self._rst.append('    %s' % badges.named(option, self.options[option]), self.c)

  def run(self):
    """Generated rendered rst.

    Data is processed to a in-memory rst list, then rendered directly to the
    current document.
    """
    self._add_dropdown_header()
    self._add_panel_template()
    self._add_update(self._sanitize_update())
    self._add_named_link('galaxy')
    self._add_named_link('source')
    self._add_named_link('service_doc', 'service docs')
    if 'private' in self.options:
      self._rst.append("    %s" % self._convert_to_badge('{PRIVATE}'), self.c)
    if 'ref' in self.options:
      for r in self._sanitize_ref():
        self._add_reference(r)

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('role', Role)
