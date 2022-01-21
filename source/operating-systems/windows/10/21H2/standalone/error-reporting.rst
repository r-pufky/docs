.. _w10-21h2-standalone-error-reporting:

Error Reporting
###############
Errors encountered on your systems are automatically sent to Microsoft,
including related metadata. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. gpo::    Disable Windows Error Reporting
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Windows Error Reporting -->
            Disable Windows Error Reporting
  :value0:  ☑, {ENABLED}
  :ref:     https://auditsquare.com/advisory/windows/error-reporting
  :update:  2021-02-19
  :open:
