.. _service-nginx-custom-error-pages:

Custom Error Pages
##################
Setup a custom `error page`_ to serve `all errors`_.

.. warning::
  The **root** for web serving must be set for both the **http** and **https**
  server, otherwise it will default to what NGINX was built with. This will
  produce hard to debug errors if the page does not load.

.. code-block:: nginx
  :caption: Set root web folder for http server.

  server {
    ...
    root /www;
    ...
  }

.. note::
  This assumes **http** is redirected to **https**; so no error block needed.

.. code-block:: nginx
  :caption: Set root web folder for https server and redirect all errors to custom page.

  server {
    root       /www;
    error_page 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 421 422 423 424 426 428 429 431 451 500 501 502 503 504 505 506 507 508 510 511 /error.html;
    location = /error.html {
      allow    all;
      internal;
      root     /www;
    }
  }

* **Must** be defined for each server block.
* Define in the server block before other rules.
* ``internal`` marks the location as internal redirect only.
* ``root`` is defined to enable image file serving for the error. Static error
  pages do not need this, but a root should be defined regardless for
  predicatable behavior.

.. literalinclude:: source/error.html
  :caption: **0644 root root** ``/www/error.html``

.. note::
  This example randomly loads a background image when the page is loaded.

.. _error page: https://stackoverflow.com/questions/27610979/nginx-custom-error-page-502-with-css-and-image-files
.. _all errors: https://blog.adriaan.io/one-nginx-error-page-to-rule-them-all.html