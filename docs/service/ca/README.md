# Certificate Authority
!!! bug "TODO"
    This section is 2 versions out of date and requires updating. General
    instructions remain the same though specifics may now be incorrect.

Run your own Certificate Authority which provides authentication and
authorization for services you own. An excellent reference for [basic CA setup
and usage](https://jamielinux.com/docs/openssl-certificate-authority/introduction.html)
is here and should be well understood before proceeding.

This will setup a functional root CA, intermediate CA and client/server
certificate signing.

!!! tip
    Only minimal certificate fields are used, any actual public usage should
    provide all fields.


## Reference

* https://www.openssl.org
