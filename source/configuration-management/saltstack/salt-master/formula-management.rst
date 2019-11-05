.. _salt-formula-management:

`Formula Management`_
#####################
Forumlas are pre-defined salt modules that are defined by users to manage a
service or setup as a unit (e.g. *templates*). `A curated list from Saltstack is
here`_.

These are stored in ``/srv/salt/template/{ENVIRONMENT}/{FORMULA}`` (see
:ref:`salt-master-file`) and are directly accessing from the same base scope,
based on configuration:

.. code-block:: bash

  ls -1 /srv/salt/template/dev/some_formula
  init.sls
  pillar_config.sls
  service.sls

.. code-block:: bash
  :caption: **0644 salt salt** ``/srv/salt/static/dev/top.sls``

  dev:
    'my_host':
      - some_formula

    'other_host':
      - some_formula
      - some_formula.pillar_config
      - some_formual.service

.. _Formula Management: https://docs.saltstack.com/en/2017.7/ref/configuration/nonroot.html
.. _A curated list from Saltstack is here: https://github.com/saltstack-formulas