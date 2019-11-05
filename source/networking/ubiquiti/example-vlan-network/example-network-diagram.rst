.. _example-network-diagram:

Example Network Diagram
#######################

.. aafig::
  :name: Example VLAN Networking Using ER-4, US-8-60W, and Unifi APs.

         'Edgerouter ER-4'
  +-----------------------------+
  | +----+ +----+ +----+ +----+ |
  | |eth0| |eth1| |eth2| |eth3| +
  | +----+ +----+ +----+ +----+ |
  +---+--------------------+----+
      |                    |
     ++                'Internet (eth3)'
     |
     |    'Unifi US-8-60W (Core)'
  +--+------------------------------+
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  | |A| |D| |W| |S| |D| |D| |A| |I| |
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  +----------+---+---------------+--+
             |   |               |
             |   |           'Unifi AP 1 (8)'
     +-------+   +-----------------------+
     |  'Unifi US-8-60W (Wired)'         |  'Unifi US-8-60W (Server)'
  +--+------------------------------+ +--+------------------------------+
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ | | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  | |A| |w| |w| |w| |I| |w| |A| |w| | | |A| |s| |s| |s| |i| |s| |A| |D| |
  | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ | | +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ |
  +------------------+--------------+ +---------------------------------+
                     |
                 'Unifi AP 2 (5)'

  'A = Trunk: All'
  'W = Trunk: Wired'
  'S = Trunk: Server'
  'I = Trunk: Wifi'
  'D = Disabled'
  'w = wired'
  's = server'
  'i = infrastructure'

Back to :ref:`example-vlan-overview`.