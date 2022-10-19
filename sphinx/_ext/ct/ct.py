# Abstract base config table template class. Do not use directly.

import inspect
from . import config
from .tables import badges
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives
from sphinx.util.nodes import nested_parse_with_titles
from docutils.parsers.rst.directives.tables import Table

class AbstractConfigTable(Table):
  """Abstract config table template class.

  Renders pseudo-tables using sphinx_panels library. Table base class is needed
  only for the make_title() functionality.

  Attributes:
    delim: String delimeter to use. Default: config.DEFAULT_DELIM.
    c: String instantiated class name.
    title: node.title object containing the directive title.
    _rst: ViewList object containing generated rst. Must be cleared before each
        render operation.
    sep: Unicode menu separator to use.
    rep: String separator replacement to use.
  """

  def __init__(self, *args, **kwargs):
    """Setup default abstract class attributes."""
    super().__init__(*args, **kwargs)
    self._rst = ViewList()
    self.title, _ = self.make_title()
    self.c = inspect.currentframe().f_locals['self'].__class__.__name__
    self.delim = config.DEFAULT_DELIM
    self.sep = self.state.document.settings.env.config.ct_separator
    self.rep = self.state.document.settings.env.config.ct_separator_replace

  def _set_delim(self):
    """Sets delimeter based on :delim:, stripping whitespace."""
    if 'delim' in self.options:
      self.delim = self.options['delim'].strip()

  def _parse_list(self, key, split=None):
    """Parse directive options on key and return sanitized python list.

    Uses self.delim to split; automatically converts badges.

    Args:
      key: String key to use for self.options dictionary.
      split: String delimeter to split on. Default: self.delim.

    Returns:
      List containing directive option with whitespace stripped,
      split on the split value.
    """
    if not split:
      split = self.delim
    return [self._convert_to_badge(x.strip()) for x in self.options[key].split(split)]

  def _add_nav_to_path(self):
    """Combines nav and path options to path, if existing."""
    if 'nav' in self.options:
      self.options['path'] = '%s %s %s' % (self.options['nav'],
                                           self.sep,
                                           self.options['path'])

  def _sanitize_path(self, sep='\n'):
    """String strips whitespace and combines to single string if needed.

    Args:
      sep: String path separator. Default: '\n'.

    Returns:
      String path with whitespace stripped, combined to a single string with
      badge replacements. or None.
    """
    self._set_delim()
    if 'path' in self.options:
      return ''.join(self._parse_list('path', sep))
    return None

  def _sanitize_data(self, limit=config.DEFAULT_VALUE_LIMIT):
    """Sanitize directive user input data for :value{0..9}:.

    Converts each to List using delim, stripping whitespace.

    Args:
      limit: Integer number of value directives.
          Default: config.DEFAULT_VALUE_LIMIT.

    Returns:
      List of Lists in order of :value{0..9}: directives, containing processed
      value options. or None.
    """
    self._set_delim()
    data = []
    for x in range(0,limit):
      value = 'value%s' % x
      if value in self.options:
        data.append(self._parse_list(value))
    if data:
      return data
    return []

  def _sanitize_update(self):
    """Strips whitespace and combines to single string if needed.

    Returns:
      String processed :update: or None.
    """
    self._set_delim()
    if 'update' in self.options:
      return ''.join(self._parse_list('update'))
    return None

  def _sanitize_ref(self):
    """Converts List using delim, stripping whitespace & combining to string.

    Returns:
      List of Strings split on delim from :ref: or None.
    """
    self._set_delim()
    if 'ref' in self.options:
      return self._parse_list('ref')
    return None

  def gen_label(self, text, space=True):
    """Generate primative text label from menuselection with badge replacement.

    Args:
      text: Unicode text to generate.
      space: Boolean True to insert a single space before and after the unicode
          separator, trimming existing whitespace as needed. False: leaves
          whitespace as is. Default: True.

    Returns:
      String containing processed label with custom separators.
    """
    if space:
      sep = ' %s ' % self.sep
      menu_text = sep.join(map(lambda x: self._convert_to_badge(x.strip()), text.split(self.rep)))
    else:
      menu_text = text.replace(self.rep, self.sep)
    return menu_text

  def _convert_to_badge(self, text):
    """Convert raw text to badge.

    Text is matched if contained within brackets {TEXT}.

    Args:
      text: String text to potentially convert.

    Requires:
      self.text_badges: Dictionary containing text:rst mappings.

    Returns:
      String raw text or rst formatted badge.
    """
    try:
      return badges.badges[text]
    except KeyError:
      return text

  def _generate_references(self):
    """Generate list of badges for the :ref: directive.

    Requires:
      ref RST directive, otherise empty list is returned.
    """
    refs = []
    if 'ref' in self.options:
      for r in self._sanitize_ref():
        refs.append(badges.ref(r))
    return refs

  def _dropdown(self, title, color='primary', icon=None, open=True, grid='1 1 1 1', indent=0):
    """Render a RST dropdown template.

    https://sphinx-design.readthedocs.io/en/latest/dropdowns.html#dropdown-options

    Args:
      title: str dropdown title.
      color: str titlebar color. Default: primary.
      icon: str octicon icon to use. Default: None.
      open: bool True to default to open. Default: True.
      grid: str grid directive text. Default: 1 1 1 1.
      indent: int number of spaces to indent RST block. Default: 0.
    """
    offset = ' ' * indent
    self._rst.append('%s.. dropdown:: %s' % (offset, title), self.c)
    self._rst.append('%s  :color: %s' % (offset, color), self.c)
    if icon:
      self._rst.append('%s  :icon: %s' % (offset, icon), self.c)
    self._rst.append('%s  :animate: fade-in' % offset, self.c)
    self._rst.append('%s  :class-container: sd-shadow-sm' % offset, self.c)
    if 'open' in self.options:
      self._rst.append('%s  :open:' % offset, self.c)
    self._rst.append('', self.c)
    self._rst.append('%s  .. grid:: 1 1 1 1' % offset, self.c)
    self._rst.append('%s    :margin: 0' % offset, self.c)
    self._rst.append('%s    :padding: 0' % offset, self.c)
    self._rst.append('%s    :gutter: 1' % offset, self.c)
    self._rst.append('', self.c)

  def _grid_item_card_horizontal_container_column(self, data=None, css='sd-border-0', indent=4):
    """Add a full row horizontal container, vertical grid.

    Args:
      data: str data to render to the card.
      css: str CSS clases to apply. Default: sd-border-0.
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._rst.append('', self.c)
    self._rst.append('%s.. grid-item-card::' % offset, self.c)
    self._rst.append('%s  :class-card: %s' % (offset, css), self.c)
    self._rst.append('%s  :margin:  0' % offset, self.c)
    self._rst.append('%s  :padding: 0' % offset, self.c)
    self._rst.append('%s  :shadow:  none' % offset, self.c)
    self._rst.append('', self.c)
    if data:
      self._rst.append('%s  %s' % (offset, repr(data)[1:-1]), self.c)
      self._rst.append('', self.c)

  def _grid_item_horizontal_container_row(self, indent=4):
    """Add a full row empty horizontal container, horizontal grid.

    Args:
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._rst.append('', self.c)
    self._rst.append('%s.. grid-item::' % offset, self.c)
    self._rst.append('%s  :columns: 12' % offset, self.c)
    self._rst.append('%s  :margin:  0' % offset, self.c)
    self._rst.append('%s  :padding: 0' % offset, self.c)
    self._rst.append('%s  :child-direction: row' % offset, self.c)
    self._rst.append('', self.c)

  def _grid_item_card_horizontal_container_path(self):
    """Convenience method to create a rendered path."""
    self._grid_item_card_horizontal_container_column(
      data=self.gen_label(self._sanitize_path()),
      css='sd-border-0 sd-font-weight-bold sd-bg-light'
    )

  def _card(self, data, css='sd-border-0', width='50%', margin=0, shadow='none', indent=4):
    """Add a standard grid card.

    Args:
      data: str data to render to the card.
      css: str CSS clases to apply. Default: sd-border-0.
      width: str card width (auto, 25%, 50%, 75%, 100%). Default: 50%.
      margin: int margin. Default 0.
      shadow: str CSS shadow class. Default: 'none'.
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._rst.append('', self.c)
    self._rst.append('%s.. card::' % offset, self.c)
    self._rst.append('%s  :class-card: %s' % (offset, css), self.c)
    self._rst.append('%s  :width: %s' % (offset, width), self.c)
    self._rst.append('%s  :margin: %s' % (offset, margin), self.c)
    self._rst.append('%s  :shadow: %s' % (offset, shadow), self.c)
    self._rst.append('', self.c)
    # repr is used to auto-escape strings for rendering in sudo-rst (e.g. \\)
    # returns quoted, so strip quotes to ensure render correctly.
    self._rst.append('%s  %s' % (offset, repr(data)[1:-1]), self.c)
    self._rst.append('', self.c)

  def _grid_item_card_horizontal_content(self, indent=4):
    """Add a full row horizontal container with content.

    Requires:
      self.content for rendering data.

    Args:
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._grid_item_card_horizontal_container_column(indent)
    for line in self.content:
      self._rst.append('%s  %s' % (offset, line), self.c)
    self._rst.append('', self.c)

  # TODO: Seems to be extra vertical space at the bottom after use?
  def _grid_item_card_horizontal_update_footer(self, *args, **kwargs):
    """Add a full row horizontal container with update badges.

    Args:
      label: (kwarg) str pre-pend label to badge list. Default: ''.
      indent: (kwarg) int number of spaces to indent. Default: 4.
      *args: str rendered badges to add.
    """
    indent = kwargs['indent'] if 'indent' in kwargs else 4
    label = kwargs['label'] if 'label' in kwargs else ''
    offset = ' ' * indent
    self._rst.append('', self.c)
    self._rst.append('%s.. grid-item-card::' % offset, self.c)
    self._rst.append('%s  :columns: 12' % offset, self.c)
    self._rst.append('%s  :class-card: sd-border-0' % offset, self.c)
    self._rst.append('%s  :margin:  0' % offset, self.c)
    self._rst.append('%s  :padding: 0' % offset, self.c)
    self._rst.append('%s  :text-align: right' % offset, self.c)
    self._rst.append('%s  :shadow:  none' % offset, self.c)
    self._rst.append('', self.c)
    self._rst.append('%s  %s %s %s' % (
        offset, label, badges.update(self._sanitize_update()), ' '.join(args)), self.c)

  def _grid_item_card_horizontal_two_column_row(self, data, bold=False, highlight=False, color='light', indent=4):
    """Add a full row horizontal two column container with content.

    Args:
      data: list of str containing row data.
      bold: bool true to bold row data (e.g. as a title). Default: False.
      hightlight: bool highlight row using color. Default: False.
      color: str index highlight color. Default: light.
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._grid_item_horizontal_container_row(indent)
    css_color = 'sd-bg-%s' % color if highlight else ''
    css_bold = 'sd-font-weight-bold' if bold else ''
    self._card(data[0], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), indent=indent+2)
    self._card(data[1], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), indent=indent+2)

  def _grid_item_card_horizontal_three_column_row(self, data, bold=False, highlight=False, color='light', indent=4):
    """Add a full row horizontal three column container with content.

    Args:
      data: list of str containing row data.
      bold: bool true to bold row data (e.g. as a title). Default: False.
      hightlight: bool highlight row using color. Default: False.
      color: str index highlight color. Default: light.
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._grid_item_horizontal_container_row(indent)
    css_color = 'sd-bg-%s' % color if highlight else ''
    css_bold = 'sd-font-weight-bold' if bold else ''
    self._card(data[0], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), indent=indent+2)
    self._card(data[1], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), indent=indent+2)
    self._card(data[2], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), indent=indent+2)

  def _grid_item_card_horizontal_four_column_row(self, data, bold=False, highlight=False, color='light', indent=4):
    """Add a full row horizontal four column container with content.

    Args:
      data: list of str containing row data.
      bold: bool true to bold row data (e.g. as a title). Default: False.
      hightlight: bool highlight row using color. Default: False.
      color: str index highlight color. Default: light.
      indent: int number of spaces to offset card. Default: 4.
    """
    offset = ' ' * indent
    self._grid_item_horizontal_container_row(indent)
    css_color = 'sd-bg-%s' % color if highlight else ''
    css_bold = 'sd-font-weight-bold' if bold else ''
    self._card(data[0], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), width='25%', indent=indent+2)
    self._card(data[1], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), width='25%', indent=indent+2)
    self._card(data[2], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), width='25%', indent=indent+2)
    self._card(data[3], css='sd-border-0 sd-rounded-0 %s %s' % (css_color, css_bold), width='75%', indent=indent+2)
