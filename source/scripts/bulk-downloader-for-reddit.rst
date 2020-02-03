.. _bulk-downloader-for-reddit:

`Bulk Downloader for Reddit`_
#############################
Download all user post content, subreddits, etc.


.. code-block:: bash
  :caption: Download all submissions from a user.

  . ~/.python-env/bulk/bin/activate
  python3 ./script.py --directory {USER} --user {USER} --submitted

Setup
*****
.. gflocation:: Important File Locations (Bulk Downloader for Reddit)
  :file:    ~/Bulk Downloader for Reddit/config.json,
            C:\Users\{USER}\Bulk Downloader for Reddit\config.json
  :purpose: Linux default configuration location.,
            Windows default configuration location.
  :no_key_title:
  :no_caption:
  :no_launch:

.. note::
  ``config.json`` can be placed in the same directory as the downloader scripts
  instead of one of these locations.

.. code-block:: bash
  :caption: Clone git repository

  git clone https://github.com/aliparlakci/bulk-downloader-for-reddit ~/git/bulk

.. code-block:: bash
  :caption: Setup python virtual environment and installation requirements.

  cd ~/.python-env
  python3 -m venv bulk
  . ~/.python-env/bulk/bin/activate

  cd ~/git/bulk
  pip install requirements.txt

.. _bulk-downloader-for-reddit-imgur:

Create Imgur API Account
========================
https://api.imgur.com/oauth2/addclient

.. gtable:: Imgur Oauth2 Client Settings
  :c0:     Application Name,
           ☑,
           Email
  :c1:     bulk,
           oauth2 without a callback URL,
           {EMAIL}
  :no_key_title:
  :no_section:
  :no_launch:

.. note::
  On success, a ``Client ID`` and ``Client Secret`` will be displayed. Use these
  to configure bulk downloader.

Initial Configuration
=====================
Requires a GUI web-browser to generate initial configuration tokens. For
headless machines, `download the latest windows release`_ and copy finished
``config.json`` to headless machine.

This assumes setup is done on Windows machine.

.. ggui:: Run simple query to generate configuration data.
  :key_title: bulk-downloader-for-reddit.exe
  :option:  download directory,
            select program mode,
            redditor,
            select sort type,
            select time filter,
            limit (0 for none)
  :setting: .,
            [4] submitted,
            {USER},
            [2] top,
            [6] all,
            1
  :no_section:
  :no_caption:
  :no_launch:

A web browser will open to imgur. Setup :ref:`bulk-downloader-for-reddit-imgur`
if not already completed.

.. gtable:: Set imgur API configuration.
  :c0:     imgur_client_id,
           imgur_client_secret
  :c1:     {IMGUR CLIENT ID},
           {IMGUR CLIENT SECRET}
  :no_key_title:
  :no_section:
  :no_launch:

A second web browser window will open to reddit.

* Login with your reddit, using two factor if needed.
* Give permission for bulk downloader to access your account by clicking
  :cmdmenu:`allow`.

.. note::
  The configuration file will be written to
  ``C:\Users\{USER}\Bulk Downloader for Reddit\config.json``

  This can be copied to the headless machine in either the script location or
  ``~/Bulk Downloader for Reddit``.

.. _Bulk Downloader for Reddit: https://github.com/aliparlakci/bulk-downloader-for-reddit
.. _download the latest windows release: https://github.com/aliparlakci/bulk-downloader-for-reddit/releases