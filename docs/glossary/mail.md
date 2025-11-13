# Mail


## DKIM
Domain Key Identified Mail: [DKIM provides][a] a method for validating a domain
name identity that is associated with an email message through cryptographic
authentication.


## DMARC
Domain-based Message Authentication, Reporting & Conformance:, is an email
authentication, policy, and reporting protocol.

It builds on the widely deployed [SPF](#spf) and [DKIM](#dkim) protocols,
adding linkage to the author ('From:') domain name, published policies for
recipient handling of authentication failures, and reporting from receivers to
senders, to improve and monitor protection of the domain from fraudulent email.


## MTA
Mail Transport Agent: handles mail server to server (e.g. other domains).


## MDA
Mail Delivery Agent: handles user access to email (e.g. IMAP).


## MUA
Mail User Agent: user client to check email (e.g. thunderbird/outlook).


## SPF
[Sender Policy Framework][b]: Email authentication method designed to detect
forging sender addresses during the delivery of the email.

[a]: http://dkim.org
[b]: https://en.wikipedia.org/wiki/Sender_Policy_Framework
