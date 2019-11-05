# .. wregedit:: Change some Registry Values
#   :key:   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
#   :names: GameDVR_Enabled, other
#   :types: DWORD,           DWORD64
#   :data:  0,               3
#   :admin:
#
#    .. note::
#       This is a free-form RST processed content for any additional
#       information pertaining to this registry change.
#
#       Metadata can be split over multiple lines.

from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class WRegEditData(config_table.ConfigTableData):
  """Structure to hold wregedit data and provide convience methods.  """
  LENGTH_MISMATCH = ('Mis-matched sets of registry key data: names, types, and '
                     'data must all contain same number of elements.')


class WRegEdit(config_table.ConfigTable):
  """Generate WRegEdit elements in a sphinx document.

  conf.py options:
    ct_wregedit_separator: Unicode separator to use for GUI menuselection. This
        uses the Unicode Character Name resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
    ct_wregedit_separator_replace: String separator to replace with Unicode
        separator. Default: '-->'.
    ct_wregedit_admin: String 'requires admin' modifier for GUI menuselection.
        Default: ' (as admin)'.
    ct_wregedit_content: String default GUI menuselection for opening regedit.
        Default: 'start --> regedit'.
    ct_wregedit_key_gui: Boolean True to display regedit key as a GUI
        menuselection, otherwise plain text. Default: True.

  Directive Options:
    key: String main registry key to modify. Required.
        e.g. HKEY_LOCAL_MACHINE\SOFTWARE\Policies.
    names: String or List of subkey names. Required. e.g. GameDVR_Enabled.
    types: String or List of subkey types. Required. e.g. DWORD.
    data: String or List of subkey data. Required. e.g. 0.
    admin: Flag enable admin requirement display in GUI menuselection.
    no_section: Flag disable the creation of section using the wregedit
        arguments, instead of a 'wregedit docutils container' block.
    show_title: Flag show wregedit table caption (caption is arguments title).
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
      self.state.document.settings.env.config.ct_wregedit_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_wregedit_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)
    self.text_content = (
      self.state.document.settings.env.config.ct_wregedit_content)
    self.key_gui = self.state.document.settings.env.config.ct_wregedit_key_gui

    if 'admin' in self.options:
      self.key_mod = self.state.document.settings.env.config.ct_wregedit_admin
    else:
      self.key_mod = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from wregedit component key.
    * Converts names, types, data to python lists with whitespace stripped;
      ensures that the three lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      WRegEditData object containing sanitized directive data.
    """
    key = ''.join([x.strip() for x in self.options['key'].split('\n')])
    names_list = [x.strip() for x in self.options['names'].split(',')]
    types_list = [x.strip() for x in self.options['types'].split(',')]
    data_list = [x.strip() for x in self.options['data'].split(',')]
    title, _ = self.make_title()

    return WRegEditData(key,
                        [names_list, types_list, data_list],
                        title,
                        cols=3,
                        gui=self.key_gui,
                        key_mod=self.key_mod)


def setup(app):
  app.add_config_value('ct_wregedit_admin', ' (as admin)', '')
  app.add_config_value('ct_wregedit_content', 'start --> regedit', '')
  app.add_config_value('ct_wregedit_key_gui', True, '')
  app.add_config_value('ct_wregedit_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_wregedit_separator_replace', config.DEFAULT_REPLACE, '')

  app.add_directive('wregedit', WRegEdit)