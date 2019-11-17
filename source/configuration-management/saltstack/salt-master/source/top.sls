prod:
  linux-base:
    - match: nodegroup
    - {STANDARD STATES}
  debian:
    - match: nodegroup
    - {DEBIAN SPECIFIC STATES}
  'host1':
    - {HOST SPECIFIC STATES}