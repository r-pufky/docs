from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table


class GFileLocationData(config_table.ConfigTableData):
  """Structure to hold config tree data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of file location data: files and '
                     'purpose must all contain same number of elements.')


class GFileLocation(config_table.ConfigTable):
  """Generate file location elements in a sphinx document.

  Directives:
    See ConfigTable for core Directives.

  .. gflocation:: Import File Locations
    :key_title: Linux File Locations
    :files:   /etc/libvirtd/,
              /var/lib/libvirt/images
    :purpose: KVM and VM configuration data.,
              Default KVM VM/ISO image pool Location.

      .. note::
        This is a free-form RST processed content contained within the rendered
        block.

        Metadata can be split over multiple lines.

  conf.py options:
    ct_gflocation_separator: Unicode separator to use for :cmdmenu:/:guilabel:
        directive. This uses the Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_gflocation_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.
    ct_gflocation_launch: String default :cmdmenu:/:guilabel: title for launching
        application.
        Default: 'File Location'.
    ct_gflocation_key_title_gui: Boolean True to render :key_title: as a
        :cmdmenu:/:guilabel:.
        Default: True.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'key_title': directives.unchanged_required,
    'files': directives.unchanged_required,
    'purpose': directives.unchanged_required,
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
      self.state.document.settings.env.config.ct_gflocation_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_gflocation_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_launch = (
        self.state.document.settings.env.config.ct_gflocation_launch)
    self.key_title_gui = (
        self.state.document.settings.env.config.ct_gflocation_key_title_gui)

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
    key_title = ''.join([x.strip() for x in self.options['key_title'].split('\n')])
    files_list = [x.strip() for x in self.options['files'].split(',')]
    purpose_list = [x.strip() for x in self.options['purpose'].split(',')]
    title, _ = self.make_title()

    return GFileLocationData(key_title,
                             [files_list, purpose_list],
                             title,
                             key_title_gui=self.key_title_gui,
                             key_title_admin_text=self.key_title_admin_text)

def setup(app):
  app.add_config_value('ct_gflocation_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_gflocation_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_gflocation_launch', 'File Location', '')
  app.add_config_value('ct_gflocation_key_title_gui', True, '')

  app.add_directive('gflocation', GFileLocation)