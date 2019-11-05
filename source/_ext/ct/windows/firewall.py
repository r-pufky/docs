# .. wfirewall:: Disable windows Defender Service
#   :key: Computer Configuration --> Administrative Templates
#   :names: Turn off Windows Defender
#   :data: Enabled
#
#    .. note::
#       This is a free-form RST processed content for any additional
#       information pertaining to this firewall change.
#
#       Metadata can be split over multiple lines.
#
# A policy section can be setup to show multiple wfirewall tables without
# additional data if multiple values are changed.
#
# .. wfirewall:: Disable windows Defender Service
#   :key: Computer Configuration --> Administrative Templates
#   :names: Turn off Windows Defender
#   :data: Enabled
#
# .. wfirewall:: Disable windows Defender Service Real-time
#   :key: Computer Configuration --> Windows Components
#   :names: Turn off real-time protection
#   :data: Enabled
#   :no_section:
#   :hide_gui:

from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table

class WFirewallData(config_table.ConfigTableData):
  """Structure to hold wfirewall data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of wfirewall key data: names and '
                     'data must all contain same number of elements.')


class WFirewall(config_table.ConfigTable):
  """Generate windows wfirewall elements in a sphinx document.

  conf.py options:
    ct_wfirewall_separator: Unicode separator to use for GUI menuselection.
        This uses the Unicode Character Name resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this over-rides ct_separator value for firewall display.
    ct_wfirewall_separator_replace: String separator to replace with Unicode
        separator. Default: '-->'.
    ct_wfirewall_admin: String 'requires admin' modifier for GUI menuselection.
        Default: ' (as admin)'.
    ct_wfirewall_content: String default GUI menuselection for opening group
        policy. Default: 'start --> gpedit.msc'.
    ct_wfirewall_key_gui: Boolean True to enable GUI menuselection display of
        firewall key. Default: True.

  Directive Options:
    key: String main firewall key to modify. Required.
        e.g. Advanced Settings --> Inbound Rules.
    names: String or List of firewall names. Required.
        e.g. Remote Desktop - Shadow (TCP-in).
    data: String or List of subkey data. Required.
        e.g. Block.
    admin: Flag enable admin requirement display in GUI menuselection.
    no_section: Flag disable the creation of section using the wfirewall
        arguments, instead of a 'wfirewall docutils container' block.
    show_title: Flag show wfirewall table caption (caption is arguments
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
      self.state.document.settings.env.config.ct_wfirewall_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_wfirewall_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_content = (
        self.state.document.settings.env.config.ct_wfirewall_content)
    self.key_gui = self.state.document.settings.env.config.ct_wfirewall_key_gui

    if 'admin' in self.options:
      self.key_mod = self.state.document.settings.env.config.ct_wfirewall_admin
    else:
      self.key_mod = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from wfirewall component key.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      WFirewallData object containing sanitized directive data.
    """
    key = ''.join([x.strip() for x in self.options['key'].split('\n')])
    names_list = [x.strip() for x in self.options['names'].split(',')]
    data_list = [x.strip() for x in self.options['data'].split(',')]
    title, _ = self.make_title()

    return WFirewallData(key,
                         [names_list, data_list],
                         title,
                         cols=2,
                         gui=self.key_gui,
                         key_mod=self.key_mod)


def setup(app):
  app.add_config_value('ct_wfirewall_admin', ' (as admin)', '')
  app.add_config_value('ct_wfirewall_content', 'start --> control panel --> system and security --> windows firewall', '')
  app.add_config_value('ct_wfirewall_key_gui', True, '')
  app.add_config_value('ct_wfirewall_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_wfirewall_separator_replace', config.DEFAULT_REPLACE, '')

  app.add_directive('wfirewall', WFirewall)