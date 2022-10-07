# Abstract base config table template class. Do not use directly.

import inspect
from . import config
from .v2 import badges
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

  def _sanitize_data(self, limit=10):
    """Sanitize directive user input data for :value{0..9}:.

    Converts each to List using delim, stripping whitespace.

    Args:
      limit: Integer number of value directives. Default: 10.

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
    """Converts to List using delim, stripping whitespace & combining to string.

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
