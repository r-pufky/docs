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
  # Account / Authorization
  '{USER}': Template.info % 'USER',
  '{PASS}': Template.info % 'PASS',
  '{EMAIL}': Template.info % 'EMAIL',
  '{TOKEN}': Template.info % 'TOKEN',
  '{KEY}': Template.info % 'KEY',
  '{SID}': Template.info % 'SID',
  '{UUID}': Template.info % 'UUID',

  # Options
  '{ON}': Template.success % 'ON',
  '{OFF}': Template.danger % 'OFF',
  '{YES}': Template.success % 'YES',
  '{NO}': Template.danger % 'NO',
  '{ACTIVE}': Template.success % 'ACTIVE',
  '{ACCEPT}': Template.success % 'ACCEPT',
  '{DROP}': Template.danger % 'DROP',
  '{DISABLE}': Template.danger % 'DISABLE',
  '{DISABLED}': Template.danger % 'DISABLED',
  '{ENABLED}': Template.success % 'ENABLED',
  '{ENABLE}': Template.success % 'ENABLE',
  '{ENTER}': Template.info % 'ENTER',
  '{ANY}': Template.info % 'ANY',
  '{SUCCESS}': Template.success % 'SUCCESS',
  '{FAILURE}': Template.danger % 'FAILURE',

  # Location / Time
  '{TZ}': Template.info % 'TZ',
  '{COUNTRY}': Template.info % 'COUNTRY',

  # Descriptors
  '{DELETE}': Template.danger % 'DELETE',
  '{DESCRIPTION}': Template.info % 'DESCRIPTION',
  '{OPTIONAL}': Template.info % 'OPTIONAL',

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

  # Networking
  '{IP}': Template.info % 'IP',
  '{!IP}': Template.info % '!IP',
  '{IP_PUB_MASK}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'NETMASK'),
  '{IP_PUB_CIDR}': '%s / %s' % (Template.info % 'PUBLIC IP', Template.info % 'CIDR'),
  '{IP_CIDR}': '%s / %s' % (Template.info % 'IP', Template.info % 'CIDR'),
  '{IP_NET_CIDR}': '%s / %s' % (Template.info % 'IP NET', Template.info % 'CIDR'),
  '{IP_RANGE}': Template.info % 'IP RANGE',
  '{GATEWAY}': Template.info % 'GATEWAY',
  '{NETWORK}': Template.info % 'NETWORK',
  '{SSH_PORT}': Template.info % 'SSH PORT',
  '{STATIC}': Template.info % 'STATIC',
  '{DHCP}': Template.info % 'DHCP',

  # Networking / DNS
  '{HOST}': Template.info % 'HOST',
  '{LOCALHOST}': Template.info % 'LOCALHOST',
  '{FQDN}': Template.info % 'FQDN',
  '{ALIAS}': Template.info % 'ALIAS',
  '{DOMAIN}': Template.info % 'DOMAIN',
  '{PUBLIC_DNS}': Template.warning % 'PUBLIC DNS',
  '{INTERNAL_DNS}': Template.info % 'INTERNAL DNS',

  # Networking / Wifi
  '{SITE}': Template.info % 'SITE',
  '{SSID}': Template.info % 'SSID',
  '{CONTROLLER}': Template.info % 'CONTROLLER',

  # Networking / Firewall
  '{PUBLIC}': Template.warning % 'PUBLIC',
  '{PRIVATE}': Template.info % 'PRIVATE',
  '{EXPOSED}': Template.warning % 'EXPOSED',
  '{RESTRICTED}': Template.info % 'RESTRICTED',
  '{TCP}': Template.info % 'TCP',
  '{UDP}': Template.info % 'UDP',
  '{TCP/UDP}': Template.info % 'TCP/UDP',

  # Networking / VLANs
  '{UPSTREAM_SWITCH}': Template.info % 'UPSTREAM SWITCH',
  '{DOWNSTREAM_SWITCH}': Template.info % 'DOWNSTREAM SWITCH',
  '{EXPECTED_SWITCH}': Template.info % 'EXPECTED SWITCH',
  '{EXPECTED_SWITCH_PORT_PROFILE}': Template.info % 'EXPECTED SWITCH PORT PROFILE',
  '{WIFI}': Template.info % 'WIFI',
  '{LOCAL}': Template.info % 'LOCAL',
  '{INTERFACE}': Template.info % 'INTERFACE',
  '{IN}': Template.info % 'IN',
  '{OUT}': Template.info % 'OUT',

  # Logging
  '{INFO}': Template.info % 'INFO',

  # Labels
  '{CAPTIVE_DNS_NAME}': '%s Captive DNS' % Template.info % 'NETWORK',
  '{CAPTIVE_DNS_EXCEPTIONS}': '%s Captive DNS Exceptions' % Template.info % 'NETWORK',
  '{DNAT_EXCEPTION_NAME}': '%s-dnat-exception-group' % Template.info % 'NETWORK',
}
