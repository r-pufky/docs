# .. ufirewall:: Define RFC1918 Private Address Space.
#   :key:   firewall/nat groups --> add group
#   :names: Name,
#           Description,
#           Type
#   :data:  RFC1918,
#           Private IPv4 address space,
#           ☑ Network Group
#
#    .. note::
#       This is a free-form RST processed content for any additional
#       information pertaining to this firewall change.
#
#       Metadata can be split over multiple lines.
#
# A firewall section can be setup to show multiple firewall tables without
# additional data if multiple values are changed.
#
# .. ufirewall:: Define RFC1918 Private Address Space.
#   :key:   firewall/nat groups --> add group
#   :names: Name,
#           Description,
#           Type
#   :data:  RFC1918,
#           Private IPv4 address space,
#           ☑ Network Group
#
# .. ufirewall:: Define RFC1918 Private Address Space.
#   :key:   firewall/nat groups --> add group
#   :names: Name,
#           Description,
#           Type
#   :data:  RFC1918,
#           Private IPv4 address space,
#           ☑ Network Group
#   :no_section:

from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class UFirewallData(config_table.ConfigTableData):
  """Structure to hold firewall data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of firewall key data: names and '
                     'data must all contain same number of elements.')


class UFirewall(config_table.ConfigTable):
  """Generate UBNT firewall elements in a sphinx document.

  conf.py options:
    ct_ufirewall_separator: Unicode separator to use for GUI menuselection.
        This uses the Unicode Character Name resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this over-rides ct_separator value for firewall display.
    ct_ufirewall_separator_replace: String separator to replace with Unicode
        separator. Default: '-->'.
    ct_ufirewall_admin: String 'requires admin' modifier for GUI menuselection.
        Default: ' (as admin)'.
    ct_ufirewall_content: String default GUI menuselection for opening group
        policy. Default: 'firewall/nat'.
    ct_ufirewall_key_gui: Boolean True to enable GUI menuselection display of
        firewall key. Default: True.

  Directive Options:
    key: String main firewall key to modify. Required.
        e.g. service --> dhcp-server.
    names: String or List of firewall names. Required.
        e.g. Enable.
    data: String or List of subkey data. Required.
        e.g. true.
    admin: Flag enable admin requirement display in GUI menuselection.
    no_section: Flag disable the creation of section using the firewall
        arguments, instead of a 'ctree docutils container' block.
    show_title: Flag show firewall table caption (caption is arguments
        title).
    hide_gui: Flag hide GUI menuselection. This also disables :admin:.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'key': directives.unchanged_required,
    'names': directives.unchanged_required,
    'types': directives.unchanged_required,
    'data': directives.unchanged_required,
    'admin': directives.flag,
    'no_section': directives.flag,
    'show_title': directives.flag,
    'hide_gui': directives.flag,
  }
  has_content = True
  add_index = True

  def __init__(self, *args, **kwargs):
    """Initalize base Table class and generate separators."""
    super().__init__(*args, **kwargs)
    self.sep = config.get_sep(
      self.state.document.settings.env.config.ct_ufirewall_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_ufirewall_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_content = (
        self.state.document.settings.env.config.ct_ufirewall_content)
    self.key_gui = self.state.document.settings.env.config.ct_ufirewall_key_gui

    if 'admin' in self.options:
      self.key_mod = self.state.document.settings.env.config.ct_ufirewall_admin
    else:
      self.key_mod = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from firewall component key.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      UFirewallData object containing sanitized directive data.
    """
    key = ''.join([x.strip() for x in self.options['key'].split('\n')])
    names_list = [x.strip() for x in self.options['names'].split(',')]
    data_list = [x.strip() for x in self.options['data'].split(',')]
    title, _ = self.make_title()

    return UFirewallData(key,
                         [names_list, data_list],
                         title,
                         cols=2,
                         gui=self.key_gui,
                         key_mod=self.key_mod)


def setup(app):
  app.add_config_value('ct_ufirewall_admin', ' (as admin)', '')
  app.add_config_value('ct_ufirewall_content', 'firewall/nat', '')
  app.add_config_value('ct_ufirewall_key_gui', True, '')
  app.add_config_value('ct_ufirewall_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_ufirewall_separator_replace', config.DEFAULT_REPLACE, '')

  app.add_directive('ufirewall', UFirewall)