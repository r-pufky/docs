# Paperless
Paperless-NGX document management.

!!! example "Migrated to ansible collection"
    Use [r_pufky.media.paperless_ngx][a].

!!! tip
    * The UID/GID should be set to a user/group that have access to your media.
      All media clients should run under the same user to run correctly.

## Suggested Archival Use
Suggested Use (based on [archivst recommendations][b]):

1. **Document Types** refer to the broad type of document in question. Is it
  a letter? Receipt? Bill? Every instance will be different, but this should
  be your broadest field. You just want to more of less get it in the
  ballpark. For example, my Receipts doctype holds receipts that I scan in,
  but it will also hold confirmations from my debtors that I paid a bill, or
  an email from Cash app that I sold Bitcoin.
2. **Correspondent** refers to the person/organization you are communicating
  with in the document. A bill from your credit card would have Capital One
  as correspondent for example, while a copy of your W2 might go under IRS.
  Again, you can be broad here, as trying to narrow it down is going to
  drive you crazy.
3. **Tags** are used to answer the below basic concepts:
  * **Who** is it referring to? In my case, I have tags for myself, my wife,
    the kids, and the dogs. They are all the same color to easily denote
    that. Note that this is NOT the same as correspondent.
  * **What** is it referring to? Is it related to your car loan? Is it
    related to your homes maintenance? Mark these tags in a different color
    to easily notice them.
  * **When** is the information in this document relevant? Was it a bill from
    2 years ago? Does it relate to your taxes for 2022? Personally, I make
    tags for the year it was received, as it makes it easier to sort. You can
    further break this down by month if needed.
4. I also make tags for special categories that I need to track. For example,
  I have a tag for any documents that we'll need for our taxes in the coming
  year, or critical documents (birth certs, etc). This helps to further
  break it down.


## Using Management Utilities
Login and switch to **paperless** user to run management utilities.

```bash
su - -s /bin/bash paperless
. /opt/paperless/src/{VERSION}/.venv/bin/activate
cd /opt/paperless/src/{VERSION}
python3 manage.py document_renamer
```

### [Reduce PDF size][c]
This will enable you to reduce pdf size if needed. Use the following settings
for specific resolutions:

* `/screen` 72dpi
* `/ebook` 150dpi
* `/prepress` 300dpi
* `/printer` 300dpi
* `/default` no change

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS={SETTING} -dNOPAUSE
-dQUIET -dBATCH -sOutputFile={OUTPUT}.pdf {INPUT}.pdf
```

### [img2pdf][d]
Included to provide increased functionality for import scripts. This will
enable lossless conversion of images to pdf's, enabling import into paperless.
The following example will strip alpha channel data from png's and convert to a
lossless pdf for import.

```bash
convert test.png -background white -alpha remove -alpha off out.png
img2pdf out.png -o import.pdf
```

### [Merge PDF's][e]
Now directly supported in Paperless.

!!! example "Actions ➔ Merge"
    Select documents in merge order.

```bash
gs -dNOPAUSE -sDEVICE=pdfwrite -dBATCH -sOutputFile={OUTPUT}.pdf {INPUT}1.pdf
{INPUT}2.pdf
```

### [Split PDF's][f]
Now directly supported in Paperless.

!!! example "Actions ➔ Split"
    Select document first.

For documents that failed consumption, manually split before re-adding to the
consumption directory.

```bash
# Repeat for each chunk of the PDF document.
gs -dBATCH -dPDFINFO {INPUT}.pdf
gs -dNOPAUSE -sDEVICE=pdfwrite -dBATCH -sOutputFile={OUTPUT}.pdf -dFirstPage=1
-dLastPage=3 {INPUT}.pdf
```


## Reverse Proxy
Reverse proxy configuration has drastically changed resulting in multiple
reported issues ([674][g], [817][h], [712][i]). Be sure to set the following
configuration variables:

``` ini
PAPERLESS_USE_X_FORWARD_HOST=true
PAPERLESS_USE_X_FORWARD_PORT=true
PAPERLESS_URL=https://paperless.example.com
PAPERLESS_CSRF_TRUSTED_ORIGINS=https://paperless.example.com
PAPERLESS_ALLOWED_HOSTS=paperless.example.com
PAPERLESS_CORS_ALLOWED_HOSTS=https://paperless.example.com
```

!!! danger "Receiving a 403 after logging in explicitly"
    Forbidden (403) CSRF verification failed. Request aborted.

See the [Proxy Rule Changes][j] and be sure to add referrer-policy to allow
requests through:

``` nginx
add_header Referrer-Policy 'strict-origin-when-cross-origin';
```

Restart both NGINX and Paperless and try again.


## Reference[^1]

[^1]: https://docs.paperless-ngx.com/administration

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/media/docs
[b]: https://old.reddit.com/r/selfhosted/comments/sdv0rr/paperless_ng_which_tags_document_types/hugenfp
[c]: https://askubuntu.com/questions/113544/how-can-i-reduce-the-file-size-of-a-scanned-pdf-file
[d]: https://github.com/josch/img2pdf
[e]: https://www.fosslinux.com/49661/merge-pdf-files-on-linux.htm
[f]: https://stackoverflow.com/questions/10228592/splitting-a-pdf-with-ghostscript
[g]: https://github.com/paperless-ngx/paperless-ngx/pull/674
[h]: https://github.com/paperless-ngx/paperless-ngx/issues/817
[i]: https://github.com/paperless-ngx/paperless-ngx/issues/712
[j]: https://github.com/paperless-ngx/paperless-ngx/wiki/Using-a-Reverse-Proxy-with-Paperless-ngx#nginx
