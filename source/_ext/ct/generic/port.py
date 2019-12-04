from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class GPortData(config_table.ConfigTableData):
  """Structure to hold config tree data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of file location data: files and '
                     'purpose must all contain same number of elements.')


class GPort(config_table.ConfigTable):
  """Generate file location elements in a sphinx document.

  Directives:
    See ConfigTable for core Directives.

    :header: Flag to render headers in the port table, below key_title.

  .. gport::    Ports Exposed
    :port:      80, 443
    :protocol:  TCP, TCP
    :type:      Public, Public
    :purpose:   HTTP webface,
                HTTPS webface
    :no_key_title:
    :header:

      .. note::
        This is a free-form RST processed content contained within the rendered
        block.

        Metadata can be split over multiple lines.

  conf.py options:
    ct_gport_separator: Unicode separator to use for :cmdmenu:/:guilabel:
        directive. This uses the Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_gport_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.
    ct_gport_launch: String default :cmdmenu:/:guilabel: title for launching
        application.
        Default: 'Ports Exposed'.
    ct_gport_key_title_gui: Boolean True to render :key_title: as a
        :cmdmenu:/:guilabel:.
        Default: True.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'port': directives.unchanged_required,
    'protocol': directives.unchanged_required,
    'type': directives.unchanged_required,
    'purpose': directives.unchanged_required,
    'header': directives.flag,
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
      self.state.document.settings.env.config.ct_gport_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_gport_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_launch = (
        self.state.document.settings.env.config.ct_gport_launch)
    self.key_title_gui = (
        self.state.document.settings.env.config.ct_gport_key_title_gui)

    self.key_title_admin_text = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from key_title.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      FileLocationData object containing sanitized directive data.
    """
    port_list = self._parse_list('port')
    protocol_list = self._parse_list('protocol')
    type_list = self._parse_list('type')
    purpose_list = self._parse_list('purpose')

    if 'header' in self.options:
      port_list.insert(0, 'Port')
      protocol_list.insert(0, 'Protocol')
      type_list.insert(0, 'Type')
      purpose_list.insert(0, 'Purpose')

    title, _ = self.make_title()

    return GPortData(None,
                     [port_list, protocol_list, type_list, purpose_list],
                     title,
                     key_title_gui=self.key_title_gui,
                     key_title_admin_text=self.key_title_admin_text)


def setup(app):
  app.add_config_value('ct_gport_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_gport_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_gport_launch', 'Ports Exposed', '')
  app.add_config_value('ct_gport_key_title_gui', True, '')

  app.add_directive('gport', GPort)