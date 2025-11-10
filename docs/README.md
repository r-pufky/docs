# Background
I created this repository as a response to people requesting I share my setup
notes for services I run in my home. These notes have been made generic enough
so that you can implement these services and setups with relative ease. Be sure
to check the [glossary](glossary/README.md) if you see unknown symbols.

## Assumptions
These notes make the following assumptions:

* You have a advanced to expert competency in Windows, OSX, and Linux.
* You are comfortable with the following shells/languages: bash, go, cmd,
  powershell.
* You are familiar with how services work on all three platforms.
* You are comfortable writing scripts.
* You can take a generalized command and figure out the specifics (e.g.
  permissions).
* You can read man pages, and Google if you need to.

## Fit & Purpose
I do not consider these setups to be *secure* in any way shape or form, these
simply get you started off on the right foot. Don't make the assumption that
since this is setup, it is secure. It most definitely is not so. These are not
setup to be massive services either -- don't use these scripts to setup your
business or corporate environment -- you're doing it wrong. For the home gamer,
proceed.

Although I haven't done anything malicious, you should never blindly run
scripts & commands from the internet.

## Bugs & Security Concerns
Use [Let's Encrypt](https://letsencrypt.org) for free SSL/TLS certs. There's
**NO REASON** to run self-signed certs anymore for hosting anything. Don't do
it. Get a Let's Encrypt Cert.

If you find any bugs or security concerns, file a bug against this project on
git hub, or submit a CL 🙃
