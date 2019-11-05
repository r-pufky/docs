# .. ucontroller:: Enable Dynamic DNS
#   :key:    service --> dhcp-server --> dynamic-dns-update
#   :names:  Enable
#   :data:   true
#
#    .. note::
#       This is a free-form RST processed content for any additional
#       information pertaining to this controller change.
#
#       Metadata can be split over multiple lines.
#
# A controller section can be setup to show multiple controller tables without
# additional data if multiple values are changed.
#
# .. ucontroller:: Enable Dynamic DNS
#   :key:    service --> dhcp-server --> dynamic-dns-update
#   :names:  Enable
#   :data:   true
#
# .. ucontroller:: Enable Dynamic DNS Option 2
#   :key:    service --> dhcp-server
#   :names:  shared-network-name
#   :data:   IOT
#   :no_section:
#   :hide_gui:

from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class UControllerData(config_table.ConfigTableData):
  """Structure to hold controller data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of controller key data: names and '
                     'data must all contain same number of elements.')


class UController(config_table.ConfigTable):
  """Generate UBNT controller elements in a sphinx document.

  conf.py options:
    ct_controller_separator: Unicode separator to use for GUI menuselection.
        This uses the Unicode Character Name resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this over-rides ct_separator value for controller display.
    ct_controller_separator_replace: String separator to replace with Unicode
        separator. Default: '-->'.
    ct_controller_admin: String 'requires admin' modifier for GUI menuselection.
        Default: ' (as admin)'.
    ct_controller_content: String default GUI menuselection for opening group
        policy. Default: 'controller'.
    ct_controller_key_gui: Boolean True to enable GUI menuselection display of
        controller key. Default: True.

  Directive Options:
    controller: String one-off ct_controller_content replacement.
        e.g. 'https://unifi.ubnt.com --> {SITE}'. Optional.
    key: String main controller key to modify. Required.
        e.g. service --> dhcp-server.
    names: String or List of controller names. Required.
        e.g. Enable.
    data: String or List of subkey data. Required.
        e.g. true.
    admin: Flag enable admin requirement display in GUI menuselection.
    no_section: Flag disable the creation of section using the controller
        arguments, instead of a 'ctree docutils container' block.
    show_title: Flag show controller table caption (caption is arguments
        title).
    hide_gui: Flag hide GUI menuselection. This also disables :admin:.
  """
  required_arguments = 1
  optional_arguments = 1
  final_argument_whitespace = True
  option_spec = {
    'controller': directives.unchanged,
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
      self.state.document.settings.env.config.ct_controller_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_controller_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_content = (
        self.state.document.settings.env.config.ct_controller_content)
    self.key_gui = self.state.document.settings.env.config.ct_controller_key_gui

    if 'admin' in self.options:
      self.key_mod = self.state.document.settings.env.config.ct_controller_admin
    else:
      self.key_mod = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from controller component key.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      UControllerData object containing sanitized directive data.
    """
    if 'controller' in self.options:
      self.text_content = self.options['controller']

    key = ''.join([x.strip() for x in self.options['key'].split('\n')])
    names_list = [x.strip() for x in self.options['names'].split(',')]
    data_list = [x.strip() for x in self.options['data'].split(',')]
    title, _ = self.make_title()

    return UControllerData(key,
                           [names_list, data_list],
                           title,
                           cols=2,
                           gui=self.key_gui,
                           key_mod=self.key_mod)


def setup(app):
  app.add_config_value('ct_controller_admin', ' (as admin)', '')
  app.add_config_value('ct_controller_content', 'https://unifi.ubnt.com --> {SITE}', '')
  app.add_config_value('ct_controller_key_gui', True, '')
  app.add_config_value('ct_controller_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_controller_separator_replace', config.DEFAULT_REPLACE, '')

  app.add_directive('ucontroller', UController)