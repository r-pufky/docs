# Custom Error Pages
Setup a custom [error page](https://stackoverflow.com/questions/27610979/nginx-custom-error-page-502-with-css-and-image-files)
to serve [all errors](https://blog.adriaan.io/one-nginx-error-page-to-rule-them-all.html).

!!! warning
    The **root** for web serving must be set for both the **http** and
    **https** server, otherwise it will default to what NGINX was built with.
    This will produce hard to debug errors if the page does not load.

Set root web folder for http server.
``` nginx
server {
  ...
  root /www;
  ...
}
```

!!! note
    This assumes **http** is redirected to **https**; so no error block needed.

Set root web folder for https server and redirect all errors to custom page.
``` nginx
server {
  root       /www;
  error_page 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 421 422 423 424 426 428 429 431 451 500 501 502 503 504 505 506 507 508 510 511 /error.html;
  location = /error.html {
    allow    all;
    internal;
    root     /www;
  }
}
```

* **Must** be defined for each server block.
* Define in the server block before other rules.
* **internal** marks the location as internal redirect only.
* **root** is defined to enable image file serving for the error. Static error
  pages do not need this, but a root should be defined regardless for
  predictable behavior.

source/error.html (1)
{ .annotate }

1. 0644 root:root

``` html
<html>
<head>
<style type=text/css>
div {
  text-align: center;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 3em;
  position: absolute;
  top: 410px;
  width: 100%;
}
body {
  background-repeat: no-repeat;
  background-position: center top;
  background-image: 1.png;
}
</style>
<script type='text/javascript'>
function background(){
  var BG = Math.ceil(Math.random() * 12);
  document.body.background = 'https://example.com/img/' + BG + '.png';
}
</script>
</head>
</html>
<body onload='background();'>
<div>Whoops.</div>
</html>
```

!!! note
    This example randomly loads a background image when the page is loaded.
