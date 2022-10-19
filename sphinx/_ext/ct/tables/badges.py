# Badges RST template configuration.

class Style(object):
  # primary='badge-primary badge-pill text-white'
  # secondary='badge-secondary badge-pill text-white'
  # info='badge-info badge-pill text-white'
  # success='badge-success badge-pill text-white'
  # danger='badge-danger badge-pill text-white'
  # warning='badge-warning badge-pill text-white'
  # light='badge-light badge-pill text-white'
  # dark='badge-dark badge-pill text-white'

  primary='-primary'
  secondary='-secondary'
  info='-info'
  success='-success'
  danger='-danger'
  warning='-warning'
  light='-light'
  dark='-dark'
  plain=''

def badge(text, type='badge', style=Style.info, link='#', tip=''):
  """Returns a templated badge containing optional link.

  Args:
    text: String badge text label.
    type: String badge type (badge, link). Default: badge.
    style: String badge style. Default: Style.info.
    link: String URI to link. Default: #.
    tip: String tooltip. Default: None.
  """
  if type.lower() == 'badge':
    return ':bdg%s:`%s`' % (style, text)
  else:
    return ':bdg-link%s:`%s <%s>`' % (style, text, link)

def ref(ref, tip=''):
  return badge('Reference', type='link', link=ref, tip=tip)

def update(text):
  return badge('Updated: %s' % text or 'Never', style=Style.secondary)

badges = {
  # Account / Authorization
  '{USER}': badge('USER'),
  '{PASS}': badge('PASS'),
  '{EMAIL}': badge('EMAIL'),
  '{TOKEN}': badge('TOKEN'),
  '{KEY}': badge('KEY'),
  '{SID}': badge('SID'),
  '{UUID}': badge('UUID'),

  # Options
  '{ON}': badge('ON', style=Style.success),
  '{OFF}': badge('OFF', style=Style.danger),
  '{YES}': badge('YES', style=Style.success),
  '{NO}': badge('NO', style=Style.danger),
  '{ACTIVE}': badge('ACTIVE', style=Style.success),
  '{ACCEPT}': badge('ACCEPT', style=Style.success),
  '{DROP}': badge('DROP', style=Style.danger),
  '{DISABLE}': badge('DISABLE', style=Style.danger),
  '{DISABLED}': badge('DISABLED', style=Style.danger),
  '{ENABLED}': badge('ENABLED', style=Style.success),
  '{ENABLE}': badge('ENABLE', style=Style.success),
  '{ENTER}': badge('ENTER'),
  '{ANY}': badge('ANY'),
  '{SUCCESS}': badge('SUCCESS', style=Style.success),
  '{FAILURE}': badge('FAILURE', style=Style.danger),
  '{EMPTY}': badge('EMPTY', style=Style.danger),
  '{BLOCK}': badge('BLOCK', style=Style.danger),

  # Location / Time
  '{TZ}': badge('TZ'),
  '{COUNTRY}': badge('COUNTRY'),

  # Descriptors / Actions
  '{ADD}': badge('ADD', style=Style.success),
  '{DELETE}': badge('DELETE', style=Style.danger),
  '{DESCRIPTION}': badge('DESCRIPTION'),
  '{OPTIONAL}': badge('OPTIONAL'),
  '{DRIVE}': badge('DRIVE'),
  '{LMB}': badge('🖯'),
  '{MMB}': badge('🖰'),
  '{RMB}': badge('🖱'),

  # Services
  '{STARTED}': badge('STARTED', style=Style.success),
  '{STOPPED}': badge('STOPPED', style=Style.danger),
  '{AUTOMATIC}': badge('AUTOMATIC'),

  # Regedit
  '{DWORD}': badge('DWORD'),
  '{REG_DWORD}': badge('DWORD'),
  '{SZ}': badge('SZ'),
  '{REG_SZ}': badge('SZ'),
  '{BINARY}': badge('BINARY'),
  '{REG_BINARY}': badge('BINARY'),
  '{DWORD_LITTLE_ENDIAN}': badge('DWORD_LITTLE_ENDIAN'),
  '{REG_DWORD_LITTLE_ENDIAN}': badge('DWORD_LITTLE_ENDIAN'),
  '{DWORD_BIG_ENDIAN}': badge('DWORD_BIG_ENDIAN'),
  '{REG_DWORD_BIG_ENDIAN}': badge('DWORD_BIG_ENDIAN'),
  '{EXPAND_SZ}': badge('EXPAND_SZ'),
  '{REG_EXPAND_SZ}': badge('EXPAND_SZ'),
  '{LINK}': badge('LINK'),
  '{REG_LINK}': badge('LINK'),
  '{MULTI_SZ}': badge('MULTI_SZ'),
  '{REG_MULTI_SZ}': badge('MULTI_SZ'),
  '{NONE}': badge('NONE'),
  '{REG_NONE}': badge('NONE'),
  '{QWORD}': badge('QWORD'),
  '{REG_QWORD}': badge('QWORD'),
  '{QWORD_LITTLE_ENDIAN}': badge('QWORD_LITTLE_ENDIAN'),
  '{REG_QWORD_LITTLE_ENDIAN}': badge('QWORD_LITTLE_ENDIAN'),

  # GPO
  '{ENTERPRISE}': badge('ENTERPRISE', style=Style.dark),
  '{EDU}': badge('EDU', style=Style.dark),
  '{PRO}': badge('PRO', style=Style.dark),
  '{HOME}': badge('HOME', style=Style.dark),

  # Networking
  '{IP}': badge('IP'),
  '{!IP}': badge('!IP'),
  '{IP_PUB_MASK}': '%s / %s' % (badge('PUBLIC IP'), badge('NETMASK')),
  '{IP_PUB_CIDR}': '%s / %s' % (badge('PUBLIC IP'), badge('CIDR')),
  '{IP_CIDR}': '%s / %s' % (badge('IP'), badge('CIDR')),
  '{IP_NET_CIDR}': '%s / %s' % (badge('IP NET'), badge('CIDR')),
  '{IP_RANGE}': badge('IP RANGE'),
  '{GATEWAY}': badge('GATEWAY'),
  '{NETWORK}': badge('NETWORK'),
  '{SSH_PORT}': badge('SSH PORT'),
  '{STATIC}': badge('STATIC'),
  '{DHCP}': badge('DHCP'),
  '{HTTPS}': badge('HTTPS'),
  '{HTTP}': badge('HTTP'),

  # Networking / DNS
  '{HOST}': badge('HOST'),
  '{LOCALHOST}': badge('LOCALHOST'),
  '{FQDN}': badge('FQDN'),
  '{ALIAS}': badge('ALIAS'),
  '{DOMAIN}': badge('DOMAIN'),
  '{PUBLIC_DNS}': badge('PUBLIC DNS', style=Style.warning),
  '{INTERNAL_DNS}': badge('INTERNAL DNS'),

  # Networking / Wifi
  '{SITE}': badge('SITE'),
  '{SSID}': badge('SSID'),
  '{CONTROLLER}': badge('CONTROLLER'),

  # Networking / Firewall
  '{PUBLIC}': badge('PUBLIC', style=Style.warning),
  '{PRIVATE}': badge('PRIVATE', style=Style.warning),
  '{EXPOSED}': badge('EXPOSED', style=Style.warning),
  '{RESTRICTED}': badge('RESTRICTED', style=Style.warning),
  '{TCP}': badge('TCP'),
  '{UDP}': badge('UDP'),
  '{TCP/UDP}': badge('TCP/UDP'),

  # Networking / VLANs
  '{UPSTREAM_SWITCH}': badge('UPSTREAM SWITCH'),
  '{DOWNSTREAM_SWITCH}': badge('DOWNSTREAM SWITCH'),
  '{EXPECTED_SWITCH}': badge('EXPECTED SWITCH'),
  '{EXPECTED_SWITCH_PORT_PROFILE}': badge('EXPECTED SWITCH PORT PROFILE'),
  '{WIFI}': badge('WIFI'),
  '{LOCAL}': badge('LOCAL'),
  '{INTERFACE}': badge('INTERFACE'),
  '{IN}': badge('IN'),
  '{OUT}': badge('OUT'),

  # Logging
  '{INFO}': badge('INFO'),

  # Labels
  '{CAPTIVE_DNS_NAME}': '%s Captive DNS' % badge('NETWORK'),
  '{CAPTIVE_DNS_EXCEPTIONS}': '%s Captive DNS Exceptions' % badge('NETWORK'),
  '{DNAT_EXCEPTION_NAME}': '%s-dnat-exception-group' % badge('NETWORK'),
}
