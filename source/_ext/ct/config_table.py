# Base config table template. Abstract classes. Do not use directly.

import inspect
from . import config
from . import cmdmenu
from docutils import nodes
from docutils.parsers.rst.directives.tables import Table


class ConfigTableData(object):
  """Structure to hold MS table data and provide convience methods.

  Attributes:
    LENGTH_MISMATCH: String detailed explanation of data mismatch.
    key: String whitespace striped main key.
    data: List of Lists containing string data to display in table. Order is
        preserved. Minimum one list.
    title: nodes.title object containing parsed directive arguments as title.
    cols: Integer number of colums for table.
    use_gui_key: Boolean True to render table key as a menuselection role.
    key_mod: String title modifier for GUI key display.
  """
  LENGTH_MISMATCH = ('Abstract ConfigTableData length mismatch error. You '
                     'should not see this.')

  def __init__(self,
               key=None,
               data=None,
               title=None,
               cols=3,
               gui=False,
               key_mod=None):
    """Initialize config table data structure with data or defaults.

    Args:
      key: String directive option key. Default: None.
      data: List of Lists containing string data to display in table.
          Order is preserved. Minimum one list.
      title: nodes.title object. Default: nodes.title().
      cols: Integer number of colums for table. Default: 3.
      gui: Boolean True to render table key as a menuselection role.
          Default: False (render as normal text).
      key_mod: String key modifier for GUI display. Default: ''.

    Raises:
      ValueError if names, types and data lists lengths do not match.
    """
    self.key = key
    self.data = data or [[]]
    self.title = title or nodes.title()
    self.cols = cols
    self.use_gui_key = gui
    self.key_mod = key_mod or ''

    required_length = len(self.data[0])
    if not all(len(lst) == required_length for lst in self.data[1:]):
      raise ValueError

  def raw_title(self):
    """Return title attribute as String."""
    return self.title.astext()

  def zip(self):
    """Return zip of all data elements together.

    Returns:
      zip() containing all list data.
    """
    return zip(*self.data)


class ConfigTable(Table):

  def run(self):
    """Run the config table generation directive.

    Determine the calling class name and label directive accordingly.

    Returns:
      List containing config table directive.
    """
    caller_name = inspect.currentframe().f_locals['self'].__class__.__name__
    directive = []

    try:
      data = self._sanitize_options()
    except ValueError as e:
      return [self.state_machine.reporter.error(
          data.LENGTH_MISMATCH,
          nodes.literal_block(self.block_text, self.block_text),
          line=self.lineno)]

    if 'no_section' in self.options:
      directive_node = nodes.container(rawsource='\n'.join(self.content),
                                       ids=[data.raw_title()])
      directive_node.set_class(caller_name)
      directive = [directive_node]
      container = directive_node
    else:
      section_target, section = self._section(data.raw_title())
      directive = [section_target, section]
      container = section

    if not 'hide_gui' in self.options:
      container += self._gui_command('%s%s' % (self.text_content, data.key_mod),
                                     self.sep,
                                     self.rep)

    container += self.build_table(data)
    self.state.nested_parse(self.content, self.content_offset, container)

    return directive

  def build_table(self, data):
    """Build a table to display values.

    Args:
      data: Data object containing source data.

    Side Effects:
      'show_title' directive option will remove the inclusion of a generated
          caption for table.

    Returns:
      nodes.table constructed with source data.
    """
    table = nodes.table()
    table_group = nodes.tgroup(cols=data.cols)
    table += table_group

    table_group.extend(
        [nodes.colspec(colwidth=1, colname='c%s' % i) for i in range(data.cols)]
    )

    table_body = nodes.tbody()
    table_group += table_body
    rows = []

    key_row = nodes.row()
    key_entry = nodes.entry(morecols=data.cols)
    if data.use_gui_key:
      key_entry += self._gui_command(data.key, self.sep, self.rep)
    else:
      key_entry += nodes.paragraph(text=data.key)
    key_row += key_entry
    rows.append(key_row)

    for element in data.zip():
      reg_row = nodes.row()
      for cell in element:
        entry = nodes.entry()
        entry += nodes.paragraph(text=cell)
        reg_row += entry
      rows.append(reg_row)
    table_body.extend(rows)

    self.add_name(table)
    if 'show_title' in self.options:
      table.insert(0, data.title)

    return table

  def _gui_command(self, text, sep, rep):
    """Render a menuselection node specifically for given text.

    Args:
      text: String content text to use. Default: gpolicy_content.
      sep: Unicode separator to use rendering menu.
      rep: String separator string to replace with Unicode string.

    Returns:
      list[nodes.Node] containing group policy menuselection data.
    """
    return cmdmenu.gen_menu(text, sep, rep)

  def _section(self, title):
    """Generate section node for given title.

    title:
      title: String title to use when creating a section.

    Returns:
      Tuple (nodes.target, nodes.section) section nodes.
    """
    target = nodes.target()
    section = nodes.section()
    section_text_nodes, _ = self.state.inline_text(title, self.lineno)
    section_title = nodes.title(title, '', *section_text_nodes)
    section += section_title
    self.state.add_target(title, '', target, self.lineno)

    return (target, section)