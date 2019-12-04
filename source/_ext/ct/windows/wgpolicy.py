from .. import config
from .. import config_table
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table

class WGroupPolicyData(config_table.ConfigTableData):
  """Structure to hold group policy data and provide convience methods."""
  LENGTH_MISMATCH = ('Mis-matched sets of group policy key data: names and '
                     'data must all contain same number of elements.')


class WGroupPolicy(config_table.ConfigTable):
  """Generate windows group policy elements in a sphinx document.

  Directives:
    See ConfigTable for core Directives.

    :admin: Flag to enable admin requirement display in :key_title:.

  .. wgpolicy:: Enable logon logoff events policy policy
    :key_title: Computer Configuration -->
                Windows Settings -->
                Security Settings -->
                Advanced Audit Policy Configuration -->
                System Audit Policies - Local Group Policy Object -->
                Logon/Logoff -->
                Audit Other Login/Logoff Events
    :option:    ☑,
                ☑,
                ☑
    :setting:   Configure the following audit events,
                Success,
                Failure
    :admin:

      .. note::
        This is a free-form RST processed content contained within the rendered
        block.

        Metadata can be split over multiple lines.

  conf.py options:
    ct_wgpolicy_separator: Unicode separator to use for :cmdmenu:/:guilabel:
        directive. This uses the Unicode Character Name to resolve a glyph.
        Default: '\N{TRIANGULAR BULLET}'.
        Suggestions: http://xahlee.info/comp/unicode_arrows.html
        Setting this overrides ct_{CLASS}_separator value for display.
    ct_wgpolicy_separator_replace: String separator to replace with
        ct_{CLASS}_separator.
        Default: '-->'.
    ct_wgpolicy_admin: String require admin modifier for :cmdmenu:/:guilabel:
        Default: ' (as admin)'.
    ct_wgpolicy_launch: String default :cmdmenu:/:guilabel: title for launching
        application.
        Default: 'Start --> gpedit.msc'.
    ct_wgpolicy_key_title_gui: Boolean True to render :key_title: as a
        :cmdmenu:/:guilabel:.
        Default: True.
  """
  required_arguments = 1
  optional_arguments = 0
  final_argument_whitespace = True
  option_spec = {
    'key_title': directives.unchanged_required,
    'option': directives.unchanged_required,
    'setting': directives.unchanged_required,
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
      self.state.document.settings.env.config.ct_wgpolicy_separator,
      self.state.document.settings.env.config.ct_separator)
    self.rep = config.get_rep(
      self.state.document.settings.env.config.ct_wgpolicy_separator_replace,
      self.state.document.settings.env.config.ct_separator_replace)

    self.text_launch = (
        self.state.document.settings.env.config.ct_wgpolicy_launch)
    self.key_title_gui = (
        self.state.document.settings.env.config.ct_wgpolicy_key_title_gui)

    if 'admin' in self.options:
      self.key_title_admin_text = (
          self.state.document.settings.env.config.ct_wgpolicy_admin)
    else:
      self.key_title_admin_text = ''

  def _sanitize_options(self):
    """Sanitize directive user input data.

    * Strips whitespace from key_title.
    * Converts names, data to python lists with whitespace stripped;
      ensures that the lists are of the same length.
    * Parses directive arguments for title.

    Returns:
      WGroupPolicyData object containing sanitized directive data.
    """
    key_title = ''.join(self._parse_list('key_title','\n'))
    option_list = self._parse_list('option')
    setting_list = self._parse_list('setting')
    title, _ = self.make_title()

    return WGroupPolicyData(key_title,
                            [option_list, setting_list],
                            title,
                            key_title_gui=self.key_title_gui,
                            key_title_admin_text=self.key_title_admin_text)


def setup(app):
  app.add_config_value('ct_wgpolicy_separator', config.DEFAULT_SEPARATOR, '')
  app.add_config_value('ct_wgpolicy_separator_replace', config.DEFAULT_REPLACE, '')
  app.add_config_value('ct_wgpolicy_admin', ' (as admin)', '')
  app.add_config_value('ct_wgpolicy_launch', 'Start --> gpedit.msc', '')
  app.add_config_value('ct_wgpolicy_key_title_gui', True, '')

  app.add_directive('wgpolicy', WGroupPolicy)