# Abstract base config table template class. Do not use directly.

import inspect
from . import config
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
    _text_badges: Dictionary containing text:rst badge mappings.
  """

  def __init__(self, *args, **kwargs):
    """Setup default abstract class attributes."""
    super().__init__(*args, **kwargs)
    self._rst = ViewList()
    self.title, _ = self.make_title()
    self.c = inspect.currentframe().f_locals['self'].__class__.__name__
    self.delim = config.DEFAULT_DELIM

  def _set_delim(self):
    """Sets delimeter based on :delim:, stripping whitespace."""
    if 'delim' in self.options:
      self.delim = self.options['delim'].strip()

  def _parse_list(self, key, split=None):
    """Parse directive options on key and return sanitized python list.

    Uses self.delim to split.

    Args:
      key: String key to use for self.options dictionary.
      split: String delimeter to split on. Default: self.delim.

    Returns:
      List containing directive option with whitespace stripped,
      split on the split value.
    """
    if not split:
      split = self.delim
    return [x.strip() for x in self.options[key].split(split)]

  def _sanitize_path(self, sep='\n'):
    """String strips whitespace and combines to single string if needed.

    Args:
      sep: String path separator. Default: '\n'.

    Returns:
      Tuple (path, data, ref, update). data is a list containing processed value
      options.
    """
    self._set_delim()
    if 'path' in self.options:
      return ''.join(self._parse_list('path',sep))
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
    return None

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
      return self._text_badges[text]
    except KeyError:
      return text
