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
  '{!IP}': Template.info % '!IP',
  '{TZ}': Template.info % 'TZ',
  '{COUNTRY}': Template.info % 'COUNTRY',
  '{DESCRIPTION}': Template.info % 'DESCRIPTION',
  '{OFF}': Template.danger % 'OFF',
  '{DISABLE}': Template.danger % 'DISABLE',
  '{DISABLED}': Template.danger % 'DISABLED',
  '{ACCEPT}': Template.success % 'ACCEPT',
  '{ON}': Template.success % 'ON',
  # Regedit
  '{DWORD}': Template.info % 'DWORD',
  '{REG_DWORD}': Template.info % 'DWORD',
  '{SZ}': Template.info % 'SZ',
  '{REG_SZ}': Template.info % 'SZ',
  '{BINARY}': Template.info % 'BINARY',
  '{REG_BINARY}': Template.info % 'BINARY',
  '{DWORD_LITTLE_ENDIAN}': Template.info % 'DWORD_LITTLE_ENDIAN',
  '{REG_DWORD_LITTLE_ENDIAN}': Template.info % 'DWORD_LITTLE_ENDIAN',
  '{DWORD_BIG_ENDIAN}': Template.info % 'DWORD_BIG_ENDIAN',
  '{REG_DWORD_BIG_ENDIAN}': Template.info % 'DWORD_BIG_ENDIAN',
  '{EXPAND_SZ}': Template.info % 'EXPAND_SZ',
  '{REG_EXPAND_SZ}': Template.info % 'EXPAND_SZ',
  '{LINK}': Template.info % 'LINK',
  '{REG_LINK}': Template.info % 'LINK',
  '{MULTI_SZ}': Template.info % 'MULTI_SZ',
  '{REG_MULTI_SZ}': Template.info % 'MULTI_SZ',
  '{NONE}': Template.info % 'NONE',
  '{REG_NONE}': Template.info % 'NONE',
  '{QWORD}': Template.info % 'QWORD',
  '{REG_QWORD}': Template.info % 'QWORD',
  '{QWORD_LITTLE_ENDIAN}': Template.info % 'QWORD_LITTLE_ENDIAN',
  '{REG_QWORD_LITTLE_ENDIAN}': Template.info % 'QWORD_LITTLE_ENDIAN',
  # GPO
  '{ENTERPRISE}': Template.dark % 'ENTERPRISE',
  '{EDU}': Template.dark % 'EDU',
  '{PRO}': Template.dark % 'PRO',
  '{HOME}': Template.dark % 'HOME',
  # Ubiquiti / Networking
  '{IP_PUB_MASK}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'NETMASK'),
  '{IP_PUB_CIDR}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'CIDR'),
  '{IP_CIDR}': '%s / %s' % (Template.info % 'IP', Template.info % 'CIDR'),
  '{IP_NET_CIDR}': '%s / %s' % (Template.info % 'IP NET', Template.info % 'CIDR'),
  '{IP_RANGE}': Template.info % 'IP RANGE',
  '{GATEWAY}': Template.info % 'GATEWAY',
  '{NETWORK}': Template.info % 'NETWORK',
  '{FQDN}': Template.info % 'FQDN',
  '{SITE}': Template.info % 'SITE',
  '{SSID}': Template.info % 'SSID',
  '{ALIAS}': Template.info % 'ALIAS',
  '{DOMAIN}': Template.info % 'DOMAIN',
  '{SSH_PORT}': Template.info % 'SSH PORT',
  '{STATIC}': Template.info % 'STATIC',
  '{DHCP}': Template.info % 'DHCP',
  '{TCP}': Template.info % 'TCP',
  '{UDP}': Template.info % 'UDP',
  '{TCP/UDP}': Template.info % 'TCP/UDP',
  '{UPSTREAM_SWITCH}': Template.info % 'UPSTREAM SWITCH',
  '{DOWNSTREAM_SWITCH}': Template.info % 'DOWNSTREAM SWITCH',
  '{EXPECTED_SWITCH}': Template.info % 'EXPECTED SWITCH',
  '{EXPECTED_SWITCH_PORT_PROFILE}': Template.info % 'EXPECTED SWITCH PORT PROFILE',
  '{WIFI}': Template.info % 'WIFI',
  '{LOCAL}': Template.info % 'LOCAL',
  '{INTERFACE}': Template.info % 'INTERFACE',
  '{IN}': Template.info % 'IN',
  '{OUT}': Template.info % 'OUT',
  '{CAPTIVE_DNS_NAME}': '%s Captive DNS' % Template.info % 'NETWORK',
  '{CAPTIVE_DNS_EXCEPTIONS}': '%s Captive DNS Exceptions' % Template.info % 'NETWORK',
  '{DNAT_EXCEPTION_NAME}': '%s-dnat-exception-group' % Template.info % 'NETWORK',
  '{CONTROLLER}': Template.info % 'CONTROLLER'
}
