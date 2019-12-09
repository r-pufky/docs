from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class GTableData(config_table.ConfigTableData):
  """Structure to hold gui data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of gui key data: left and '
                     'right must all contain same number of elements.')


class GTable(config_table.ConfigTable):
  """Generate UBNT GUI elements in a sphinx document.

  Directives:
    See ConfigTable for core Directives. Up to 10 column directives.

    :admin: Flag to enable admin requirement display in :key_title:.

  .. gtable::  Services Used
    :header:   Service,
               Purpose
    :c0:       SSH,
               CRD
    :c{1..9}: SSHFS remote file access for copying videos.,
               Chrome Remote Desktop for remote login.

      .. note::
        This is a free-form RST processed content contained within the rendered
        block.

        Metadata can be split over multiple lines.

  conf.py options:
    ct_gtable_separator: Unicode separator to use for :cmdmenu:/:guilabel:
        directive. This uses the Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_gtable_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.
    ct_gtable_admin: String require admin modifier for :cmdmenu:/:guilabel:
        Default: ' (as admin)'.
    ct_gtable_launch: String default :cmdmenu:/:guilabel: title for launching
        application.
        Default: 'start --> gpedit.msc'.
    ct_gtable_key_title_gui: Boolean True to render :key_title: as a
        :cmdmenu:/:guilabel:.
        Default: True.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'key_title': directives.unchanged_required,
    'header': directives.unchanged,
    'c0': directives.unchanged_required,
    'c1': directives.unchanged,
    'c2': directives.unchanged,
    'c3': directives.unchanged,
    'c4': directives.unchanged,
    'c5': directives.unchanged,
    'c6': directives.unchanged,
    'c7': directives.unchanged,
    'c8': directives.unchanged,
    'c9': directives.unchanged,
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
      self.state.document.settings.env.config.ct_gtable_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_gtable_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_launch = (
        self.state.document.settings.env.config.ct_gtable_launch)
    self.key_title_gui = (
        self.state.document.settings.env.config.ct_gtable_key_title_gui)

    if 'admin' in self.options:
      self.key_title_admin_text = (
          self.state.document.settings.env.config.ct_gtable_admin)
    else:
      self.key_title_admin_text = ''

  def _generate_column_data(self):
    """Generate column data for table.

    Returns:
      List of lists containining columns to render, including headers if the
      directive is used.
    """
    data = []
    if 'header' in self.options:
      headers = self._parse_list('header')

    for x in range(0,10):
      column = 'c%s' % x
      if column in self.options:
        data.append(self._parse_list(column))
        if 'header' in self.options:
          data[-1].insert(0, headers[x])

    return data

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from key_title.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      GuiData object containing sanitized directive data.
    """
    if 'key_title' in self.options:
      key_title = ''.join(self._parse_list('key_title','\n'))
    else:
      key_title = ''
    title, _ = self.make_title()

    return GTableData(key_title,
                      self._generate_column_data(),
                      title,
                      key_title_gui=self.key_title_gui,
                      key_title_admin_text=self.key_title_admin_text)


def setup(app):
  app.add_config_value('ct_gtable_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_gtable_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_gtable_admin', ' (as admin)', '')
  app.add_config_value('ct_gtable_launch', 'Table', '')
  app.add_config_value('ct_gtable_key_title_gui', True, '')

  app.add_directive('gtable', GTable)
