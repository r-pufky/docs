.. _service-email-mta:

MTA/MDA
#######
The :term:`MTA` handles the transmission of email to and from the system, while
the :term:`MDA` handles delivery of email on that system.

In this configuration, *postfix* is the MTA and *dovecot* is the MDA.

See `Email Docker and Documentation`_.

#. :ref:`service-email-mta-setup`.
#. :ref:`service-email-mta-configuration`.
#. :ref:`service-email-mta-testing`.

.. rubric:: References

#. `Postfix Configuration Documentation <http://www.postfix.org/>`_
#. `Dovecot postfix debian alternative example <https://github.com/sovereign/sovereign/blob/master/roles/mailserver/templates/etc_postfix_main.cf.j2>`_

.. _Email Docker and Documentation: https://hub.docker.com/r/tvial/docker-mailserver/

.. toctree::
   :hidden:
   :maxdepth: -1

   setup
   configuration
   testing
