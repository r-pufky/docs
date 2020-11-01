.. _w10-1903-reasonable-privacy-manual:

Manual Setting Privacy Options
##############################
:cmdmenu:`⌘ + r --> ms-settings:privacy`

**Strongly** recommend using :term:`GPO` and :term:`Registry` to apply settings
consistently. See other sections in :ref:`w10-1903-reasonable-privacy`.

* Disable `all options on all 24 pages`_ and re-enable to taste.
* `Disable Ad Tracking`_.
* :cmdmenu:`Background Apps` Leave background service enable, but disable
  all apps. This will prevent searching from the start menu from breaking.

  .. note::
    If start menu searches start to fail, it is because background apps
    service has been disabled. See :ref:`w10-background-apps`.

* :cmdmenu:`Microphone` Leave enabled, but disable all apps. This will allow
  mumble to use the microphone. See `1803 update breaks microphone`_.

.. _all options on all 24 pages: https://bgr.com/2015/07/31/windows-10-upgrade-spying-how-to-opt-out/
.. _1803 update breaks microphone: https://www.ghacks.net/2018/05/01/all-the-issues-of-windows-10-version-1803-you-may-run-into/
.. _Disable Ad Tracking: https://account.microsoft.com/privacy/ad-settings/signedout?ru=https%3A%2F%2Faccount.microsoft.com%2Fprivacy%2Fad-settings
