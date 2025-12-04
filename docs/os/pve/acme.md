# ACME
Use Let's Encrypt certificates for PVE cluster nodes with Google Cloud DNS.


## Setup ACME in PVE Datacenter
Applies to **all** nodes.

!!! example "Datacenter ➔ ACME ➔ Accounts ➔ Add"
    * Account Name: **staging**
    * E-Mail: **user@example.com**
    * ACME Directory: **Let's Encrypt V2 Staging**
    * Accept TOS: ✔

!!! example "Datacenter ➔ ACME ➔ Accounts ➔ Add"
    * Account Name: **prod**
    * E-Mail: **user@example.com**
    * ACME Directory: **Let's Encrypt V2**
    * Accept TOS: ✔

!!! example "Datacenter ➔ ACME ➔ Challenge Plugins ➔ Add"
    * Plugin ID: **gcloud**
    * Validation Delay: **120**  # SLA for glcoud DNS.
    * DNS API: **gcloud**
    * API Data:
        ``` bash
        HOME=/home/nobody
        CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE=/home/nobody/pve_acme.json
        CLOUDSDK_CORE_PROJECT={PROJECT_ID}
        ```


## Add Google Cloud SDK
Add for **all** cluster nodes.

``` bash
# Add signing key.
curl -o /usr/share/keyrings/cloud.google.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

!!! abstract "/etc/apt/sources.list.d/google-cloud-sdk.sources"
    0644 root:root
    ``` bash
    Types: deb
    URIs: http://packages.cloud.google.com/apt/
    Suites: cloud-sdk
    Components: main
    Signed-By: /usr/share/keyrings/cloud.google.gpg
    ```

``` bash
# Install Google Cloud SDK and init project as ROOT.
apt-get update && apt-get install google-cloud-sdk

gcloud init
> Welcome! This command will take you through the configuration of gcloud.
>
> Your current configuration has been set to: [default]
>
> You can skip diagnostics next time by using the following flag:
>   gcloud init --skip-diagnostics
>
> Network diagnostic detects and fixes local network connection issues.
> Checking network connection...done.
> Reachability Check passed.
> Network diagnostic passed (1/1 checks passed).

You must sign in to continue. Would you like to sign in (Y/n)?  y

> Go to the following link in your browser, and complete the sign-in prompts:
>
>     https://accounts.google.com/o/oauth2/auth?response_type={AUTH_CODE}

# Copy link and use local browser to authenticate. Copy auth code.

Once finished, enter the verification code provided in your browser: {AUTH_CODE}

> You are signed in as: [user@example.com].
>
> Pick cloud project to use:
>  [1] {PROJECT_ID}
>  [3] Enter a project ID
>  [4] Create a new project

Please enter numeric choice or text value (must exactly match list item):  1
> Your current project has been set to: [{PROJECT_ID}].
> ...
```

``` bash
# Add ACME configuration for nobody user.
mkdir -p /home/nobody/.config
cp pve_acme.json /home/nobody/pve_acme.json
chmod 0600 /home/nobody/pve_acme.json
chown -R nobody:nogroup /home/nobody
```


## Add ACME Certificates
Add for **all** cluster nodes.

!!! example "Datacenter ➔ {NODE} ➔ System ➔ Certificates ➔ ACME ➔ Add"
    * Challenge Type: **DNS**
    * Domain: **{NODE}.example.com**

!!! example "Datacenter ➔ {NODE} ➔ System ➔ Certificates ➔ ACME"
    * Using Account: **staging**


!!! example "Datacenter ➔ {NODE} ➔ System ➔ Certificates ➔ Order Certificates"
    Once completed switch to **prod** and re-order certificates to finish.

    Staging certificate will automatically be removed.


## Reference[^1][^2]

[^1]: https://forum.proxmox.com/threads/google-domains-and-lets-encrypt-certificates-using-dns-validation-for-local-proxmox-servers.70337/
[^2]: https://pve.proxmox.com/wiki/Certificate_Management