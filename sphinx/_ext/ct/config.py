# Default configuration values for config table sphinx extensions.

import re

DEFAULT_SEPARATOR = r'\N{TRIANULAR_BULLET}'
DEFAULT_REPLACE = '-->'
DEFAULT_DELIM = ','
AMP_RE = re.compile(r'(?<!&)&(?![&\s])')

def _determine_preference(default, custom=None, config=None):
  """Determine the preference to use for given inputs.

  Args:
    default: Unicode DEFAULT_* preference.
    custom: Unicode custom (directive/role) preference.
    config: Unicode config preference.

  Returns:
    Unicode:
      * Custom used if not default value and set.
      * Config used if not default value and custom not set.
      * DEFAULT_* used if all defaults or none defined.
  """
  if custom and custom != default:
    return custom
  if config and config != default:
    return config
  return default

def get_sep(custom=None, config=None):
  """Determine the separator to use for given inputs.

  Args:
    custom: Unicode custom (directive/role) separator.
    config: Unicode config separator.

  Returns:
    Unicode:
      * Custom used if not default value and set.
      * Config used if not default value and custom not set.
      * DEFAULT_SEPARATOR used if all defaults or none defined.
  """
  return _determine_preference(DEFAULT_SEPARATOR, custom, config)

def get_rep(custom=None, config=None):
  """Determine the replacement to use for given inputs.

  Args:
    custom: Unicode custom (directive/role) replacement.
    config: Unicode config replacement.

  Returns:
    Unicode:
      * Custom used if not default value and set.
      * Config used if not default value and custom not set.
      * DEFAULT_REPLACE used if all defaults or none defined.
  """
  return _determine_preference(DEFAULT_REPLACE, custom, config)
