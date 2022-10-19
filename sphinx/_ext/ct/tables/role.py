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
    :galaxy:       String link to ansible galaxy repository.
    :source:       String link to ansible source repository.
    :service_doc:  String link to role service docs (e.g. manuals).
    :ref:          List of reference URI's.
    :update:       String datetime last time references/settings were checked.
    :delim:        Custom delimeter to use instead of config.DEFAULT_DELIM.
    :generic:      Use generic 'Files' dropdown label, in light-grey.
    :private:      Set to flag role as a non-exported role.
    :blocking:     Flag as OS distribution upgrade blocking with message.
    :non_blocking: Flag as OS distribution upgrade non-blocking with message.
    :open:         Set to expand the dropdown by default.

  Examples:
    .. role:: radarr
      :galaxy:      https://galaxy.ansible.com/r_pufky/radarr
      :source:      https://github.com/r-pufky/ansible_radarr
      :service_doc: https://wiki.servarr.com/radarr
      :ref:         https://some.reference.site,
                    https://some.reference.site2
      :blocking:    Requires new OS package updates.
      :private:
      :update: 2021-01-01
      :open:

      Dropdown opened by default, using commas as delim.

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
    'blocking': directives.unchanged,
    'non_blocking': directives.unchanged,
    'open': directives.flag,
    'generic': directives.flag,
  }

  def _add_blocking_badge(self):
    if 'blocking' in self.options:
      return '%s OS Distribution upgrades REQUIRE: %s' % (badges.badge('BLOCKING', style=badges.Style.danger), self.options['blocking'])
    if 'non_blocking' in self.options:
      return '%s %s' % (badges.badge('NON BLOCKING', style=badges.Style.success), self.options['non_blocking'])

  def _add_horizontal_blocking(self):
    self._grid_item_card_horizontal_container_column()
    self._rst.append("", self.c)
    self._rst.append("      %s" % self._add_blocking_badge(), self.c)
    self._rst.append("", self.c)

  def _add_named_link(self, option, text=None):
    """Add RST row for :ref: directive.

    Args:
      option: String directive option text to render badge link.
      text: String override option key with specific text for badge link.
    """
    if option in self.options:
      if text:
        return badges.badge(text, type='link', link=self.options[option])
      else:
        return badges.badge(option, type='link', link=self.options[option])

  def run(self):
    """Generated rendered rst.

    Data is processed to a in-memory rst list, then rendered directly to the
    current document.
    """
    self._dropdown('Ansible Role: %s' % self.title.astext(), icon='repo')
    self._grid_item_card_horizontal_content()
    self._add_horizontal_blocking()
    self._grid_item_card_horizontal_update_footer(
        self._add_named_link('galaxy') if 'galaxy' in self.options else '',
        self._add_named_link('source') if 'source' in self.options else '',
        self._add_named_link('service_doc', 'service docs') if 'service_doc' in self.options else '',
        *self._generate_references(),
        badges.badge('PRIVATE', style=badges.Style.warning) if 'private' in self.options else '',
        label='Role Details:')

    node = nodes.section()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self._rst, node)

    return node.children

def setup(app):
  app.add_directive('role', Role)
