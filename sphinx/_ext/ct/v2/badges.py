# Badges RST template configuration.

class Template(object):
  primary=':badge:`%s,badge-primary badge-pill`'
  secondary=':badge:`%s,badge-secondary badge-pill`'
  info=':badge:`%s,badge-info badge-pill`'
  success=':badge:`%s,badge-success badge-pill`'
  danger=':badge:`%s,badge-danger badge-pill`'
  warning=':badge:`%s,badge-warning badge-pill`'
  light=':badge:`%s,badge-light badge-pill`'
  dark=':badge:`%s,badge-dark badge-pill`'
  ref=':link-badge:`%s,"Reference",cls=badge-info badge-pill`'

def ref(ref):
  return '%s' % (Template.ref % ref)

def update(text):
  return '%s' % (Template.secondary % ('Updated: %s' % text or 'Never'))

# Generic
DELETE=Template.danger % 'DELETE'
USER=Template.success % 'USER'
PASS=Template.success % 'PASS'
HOST=Template.success % 'HOST'

# Regedit
DWORD=':badge:`DWORD,badge-info badge-pill`'
SZ=':badge:`SZ,badge-info badge-pill`'
BINARY=':badge:`BINARY,badge-info badge-pill`'
DWORD_LITTLE_ENDIAN=':badge:`DWORD_LITTLE_ENDIAN,badge-info badge-pill`'
DWORD_BIG_ENDIAN=':badge:`DWORD_BIG_ENDIAN,badge-info badge-pill`'
EXPAND_SZ=':badge:`EXPAND_SZ,badge-info badge-pill`'
LINK=':badge:`LINK,badge-info badge-pill`'
MULTI_SZ=':badge:`MULTI_SZ,badge-info badge-pill`'
NONE=':badge:`NONE,badge-info badge-pill`'
QWORD=':badge:`QWORD,badge-info badge-pill`'
QWORD_LITTLE_ENDIAN=':badge:`QWORD_LITTLE_ENDIAN,badge-info badge-pill`'

# GPO
ENTERPRISE=':badge:`ENTERPRISE,badge-dark badge-pill`'
EDU=':badge:`EDU,badge-dark badge-pill`'
PRO=':badge:`PRO,badge-dark badge-pill`'
HOME=':badge:`HOME,badge-dark badge-pill`'
