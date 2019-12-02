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
  """Generate windows registry editor elements in a sphinx document.

  Directives:
    See ConfigTable for core Directives.

    :admin: Flag to enable admin requirement display in :key_title:.

  .. wregedit:: Disable disk space warning checks for partition regedit
    :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                Policies\Explorer
    :names:     NoLowDiskSpaceChecks
    :types:     DWORD
    :data:      1
    :admin:

      .. note::
        This is a free-form RST processed content contained within the rendered
        block.

        Metadata can be split over multiple lines.

  conf.py options:
    ct_wregedit_separator: Unicode separator to use for :cmdmenu:/:guilabel:
        directive. This uses the Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_wregedit_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.
    ct_wregedit_admin: String require admin modifier for :cmdmenu:/:guilabel:
        Default: ' (as admin)'.
    ct_wregedit_launch: String default :cmdmenu:/:guilabel: title for launching
        application.
        Default: 'Start --> regedit.msc'.
    ct_wregedit_key_title_gui: Boolean True to render :key_title: as a
        :cmdmenu:/:guilabel:.
        Default: True.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'key_title': directives.unchanged_required,
    'names': directives.unchanged_required,
    'types': directives.unchanged_required,
    'data': directives.unchanged_required,
    'admin': directives.flag,
    'no_section': directives.flag,
    'no_launch': directives.flag,
    'no_caption': directives.flag,
    'no_key_title': directives.flag,
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

    self.text_launch = (
      self.state.document.settings.env.config.ct_wregedit_launch)
    self.key_title_gui = (
      self.state.document.settings.env.config.ct_wregedit_key_title_gui)

    if 'admin' in self.options:
      self.key_title_admin_text = (
          self.state.document.settings.env.config.ct_wregedit_admin)
    else:
      self.key_title_admin_text = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from key_title.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      WRegEditData object containing sanitized directive data.
    """
    key_title = ''.join([x.strip() for x in self.options['key_title'].split('\n')])
    names_list = [x.strip() for x in self.options['names'].split(',')]
    types_list = [x.strip() for x in self.options['types'].split(',')]
    data_list = [x.strip() for x in self.options['data'].split(',')]
    title, _ = self.make_title()

    return WRegEditData(key_title,
                        [names_list, types_list, data_list],
                        title,
                        key_title_gui=self.key_title_gui,
                        key_title_admin_text=self.key_title_admin_text)


def setup(app):
  app.add_config_value('ct_wregedit_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_wregedit_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_wregedit_admin', ' (as admin)', '')
  app.add_config_value('ct_wregedit_launch', 'Start --> regedit.msc', '')
  app.add_config_value('ct_wregedit_key_title_gui', True, '')

  app.add_directive('wregedit', WRegEdit)