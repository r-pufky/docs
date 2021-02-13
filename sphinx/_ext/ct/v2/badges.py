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

badges = {
  # Generic
  '{DELETE}': Template.danger % 'DELETE',
  '{USER}': Template.info % 'USER',
  '{PASS}': Template.info % 'PASS',
  '{EMAIL}': Template.info % 'EMAIL',
  '{HOST}': Template.info % 'HOST',
  '{IP}': Template.info % 'IP',
  '{DESCRIPTION}': Template.info % 'DESCRIPTION',
  # Regedit
  '{DWORD}': Template.info % 'DWORD',
  '{SZ}': Template.info % 'SZ',
  '{BINARY}': Template.info % 'BINARY',
  '{DWORD_LITTLE_ENDIAN}': Template.info % 'DWORD_LITTLE_ENDIAN',
  '{DWORD_BIG_ENDIAN}': Template.info % 'DWORD_BIG_ENDIAN',
  '{EXPAND_SZ}': Template.info % 'EXPAND_SZ',
  '{LINK}': Template.info % 'LINK',
  '{MULTI_SZ}': Template.info % 'MULTI_SZ',
  '{NONE}': Template.info % 'NONE',
  '{QWORD}': Template.info % 'QWORD',
  '{QWORD_LITTLE_ENDIAN}': Template.info % 'QWORD_LITTLE_ENDIAN',
  # GPO
  '{ENTERPRISE}': Template.dark % 'ENTERPRISE',
  '{EDU}': Template.dark % 'EDU',
  '{PRO}': Template.dark % 'PRO',
  '{HOME}': Template.dark % 'HOME',
  # Ubiquiti / Networking
  '{IP_PUB_MASK}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'NETMASK'),
  '{IP_PUB_CIDR}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'CIDR'),
  '{GATEWAY}': Template.info % 'GATEWAY',
  '{NETWORK}': Template.info % 'NETWORK',
  '{FQDN}': Template.info % 'FQDN',
  '{ALIAS}': Template.info % 'ALIAS',
  '{IP RANGE}': Template.info % 'IP RANGE',
  '{DOMAIN}': Template.info % 'DOMAIN',
  '{SSH_PORT}': Template.info % 'SSH PORT',
}
