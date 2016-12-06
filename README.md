Docs: A collection of setup notes
---------------------------------
I created this repository as a response to people requesting I share my setup
notes for services I run in my home. These notes have been made generic enough
so that you can implement these services and setups with relative ease.

Assumptions
-----------
These notes make the following assumptions

1. You have a advanced to expert competency in Windows, OSX, and Linux
2. You are comfortable with the following shells: bash, cmd and powershell
3. You are familiar with how services work on all three platforms (see #1)
4. You are comfortable writing scripts
5. You can take a generalized command and figure out the specifics
   (e.g. permissions)
6. You can read man pages, and Google if you need to

Fit & Purpose
-------------
I do not consider these setups to be 'secure' in any way shape or form, these
simply get you started off on the right foot. Don't make the assumption that
since this is setup, it is secure. It most definitely is not so. These are not
setup to be massive services either -- don't use these scripts to setup your
business or corporate environment -- you're doing it wrong. For the home gamer,
proceed.

Although I haven't done anything malicious, you should never blindly run
scripts & commands from the internet.

Bugs & Security Concerns
------------------------
If you find any bugs or security concerns, file a bug against this project on
git hub, or submit a CL :)

Reference Materials
-------------------
1. https://letsencrypt.org/ -- Free SSL/TLS certs. There's **NO REASON** to run
   self-signed certs anymore. Don't do it. Get you a Let's Encrypt Cert.
