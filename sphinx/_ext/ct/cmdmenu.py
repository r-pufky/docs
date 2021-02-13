# :cmdmenu:`start --> app`
#   Role for menuselection with custom separator.
#
#   Basic menuselection role is here:
#      https://github.com/sphinx-doc/sphinx/blob/master/sphinx/roles.py#L382
#
#    conf.py options:
#      ms_cmdmenu_separator: Unicode separator to use for GUI menuselection.
#          If defined outside the default value, this will take precedence over
#          `ct_separator`. Default: '\N{TRIANGULAR BULLET}'.
#      ms_cmdmenu_separator_replace: String to replace with the cmdmenu
#          separator. If defined outside the default value, this will take
#          precedence over `ct_separator_replace`. Default: '-->'.
#      ms_cmdmenu_replace_use_space: Boolean True to insert a single space
#          before and after the unicode separator, trimming existing whitespace
#          as needed. False: leaves whitespace as is. Default: True.

from . import config
from docutils import nodes
from docutils.parsers.rst import roles
from sphinx.util.docutils import SphinxRole

def gen_menu(text, sep, rep, space=True):
  """Generate menuselection role with specified options.

  Args:
    text: Unicode text to generate.
    sep: Unicode menu separator to use.
    rep: String separator replacement to use.
    space: Boolean True to insert a single space before and after the unicode
        separator, trimming existing whitespace as needed. False: leaves
        whitespace as is. Default: True.

  Returns:
    List[nodes.Node] containing the rendered menuselection with custom
    separator.
  """
  if space:
    sep = ' %s ' % sep
    menu_text = sep.join(map(lambda x: x.strip(), text.split(rep)))
  else:
    menu_text = text.replace(rep, sep)
  menu_node = nodes.inline(rawtext=menu_text, classes=['guilabel'])
  spans = config.AMP_RE.split(menu_text)
  menu_node += nodes.Text(spans.pop(0))

  for span in spans:
    span = span.replace('&&', '&')
    letter = nodes.Text(span[0])
    accelerator = nodes.inline('', '', letter, classes=['accelerator'])
    menu_node += accelerator
    menu_node += nodes.Text(span[1:])

  return menu_node


class CmdMenu(SphinxRole):
  """cmdmenu role to generate a gui menuselection with custom separator.

  :cmdmenu:`start --> app`
    Role for menuselection with custom separator.

  conf.py options:
    ms_cmdmenu_separator: Unicode separator to use for GUI menuselection.
        If defined outside the default value, this will take precedence over
        `ct_separator`. Default: '\N{TRIANGULAR BULLET}'.
    ms_cmdmenu_separator_replace: String to replace with the cmdmenu
        separator. If defined outside the default value, this will take
        precedence over `ct_separator_replace`. Default: '-->'.
    ms_cmdmenu_replace_use_space: Boolean True to insert a single space
        before and after the unicode separator, trimming existing whitespace
        as needed. False: leaving whitespace as is. Default: True.
  """

  def run(self):
    sep = config.get_sep(
        self.inliner.document.settings.env.config.ct_cmdmenu_separator,
        self.inliner.document.settings.env.config.ct_separator)

    rep = config.get_rep(
        self.inliner.document.settings.env.config.ct_cmdmenu_separator_replace,
        self.inliner.document.settings.env.config.ct_separator_replace)

    return [gen_menu(self.text, sep, rep)], []


def setup(app):
  app.add_config_value('ct_cmdmenu_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_cmdmenu_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_cmdmenu_replace_use_space', True, '')

  roles.register_local_role('cmdmenu', CmdMenu())
