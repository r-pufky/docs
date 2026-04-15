# [Troubleshooting][a]

## HTTP 500 Error During Import
Typically due to Paperless updating classification models and not rebuilding
the **classification_model.pickle** object:

!!! danger "logs"
    ``` log
    [ERROR] [paperless.classifier] Unknown error while loading document classification model
    ```

``` bash
# Remove the classification model and restart all services.
rm paperless_ngx_cfg_data_dir/classification_model.pickle
systemctl restart paperless_*
```

## PDF's fail to ingest with older ICC profiles.
Some PDF's with [older ICC profiles][b] may fail to be ingested. Though rare,
these can be manually pre-processed to fix the ICC profiles:

``` bash
gs -o output.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress input.pdf
```

## PDF failed import from consumption directory.
Paperless does not clean cache aggressively and TMPFS is typically cleared only
on boot. In cases where there are mass processing of documents it is better to
use disk. Some paperless subprocesses will always use **/tmp**.

Check logs for specific errors. Increase backing space if necessary and restart
the machine or the consumption service:

``` bash
systemctl restart paperless_consumer.service
```

!!! tip "Tasks may also be restarted in the django admin interface"
    Settings ➔ Open Django Admin ➔ Paperless tasks

``` bash
# The service may also be stopped and and **/tmp** cleared
systemctl stop paperless_*
rm -rf /tmp/paperless*
rm -rf {PAPERLESS_CONVERT_TMPDIR}
systemctl start paperless_*
```

[a]: https://docs.paperless-ngx.com/troubleshooting
[b]: https://kcore.org/2021/05/08/paperless-ng
