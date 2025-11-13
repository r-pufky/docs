# Operating Systems


## LDAP
Lightweight Directory Access Protocol. Directory service that offers dedicated
data storage and APIs for accessing stored information. It functions
independently of Active Directory and can function as a standalone data store
or can replicate data.


## IRM
Information Rights Management. Form of IT security technology used to protect
documents containing sensitive information from unauthorized access. Unlike
traditional Digital Rights Management (DRM) that applies to mass-produced media
like songs and movies, IRM applies to documents, spreadsheets, and
presentations created by individuals. IRM protects files from unauthorized
copying, viewing, printing, forwarding, deleting, and editing.


## Windows

### BSOD
Blue Screen of Death. Windows crash.

### Junction
Windows version of a [symlink][a].

### AD
Active Directory. Provides centralized management of network resources, user
identities, and security settings.

#### AD DS
Active Directory Domain Services. Provides directory services for managing
Windows-based computers on a network. AD DS stores information about objects
such as users, groups, computers, and other resources, and provides
authentication and authorization services.

#### DC
Domain Controller. Network server that responds to security authentication
requests and authorizes host access to domain resources. This server enforces
security policies, authenticates registered users, and stores important user
account information. Domain controllers manage and secure domain networks by
only allowing authorized users access to directory services while denying
unauthorized access.

#### AD LDS
Lightweight Directory Services. [LDAP](#ldap) for [AD](#ad).

#### AD FS
Federation Services. Allows secure sharing of identity information between
trusted business partners. It is based on industry standards and facilitates
federations across extranets, enabling trusted partners to share sensitive
identity data.

#### AD RMS
Rights Management Services. Enables users and admins to control access
permissions for sensitive documents, workbooks, and presentations. By utilizing
[IRM](#irm) policies, unauthorized individuals are prevented from duplicating
and disseminating the restricted information.

#### AD CS:
Active Directory Certificate Services. Windows server designed to issue digital
certificates. AD CS offers digital certificates that have a wide range of
applications, including the encryption and digital signing of documents and
messages, as well as authenticating computer, user, or device accounts on a
network. Certificates granted are valid for a specified period and can be
renewed or revoked as needed, providing granular control over the certificates'
lifespan.

#### GPO
Group Policy for Windows. Provides centralized management and configuration of
operating systems, applications, and users' settings.

The most restrictive GPO is applied if both machine and user GPO's are set.

Policies can be manually applied with:

``` powershell
gpupdate /force
```

#### Registry
Hierarchical database that stores low-level settings for Windows and
applications that opt to use the registry.

#### WSL
Windows Subsystem for Linux. Run linux in Windows.

[a]: https://learn.microsoft.com/en-us/windows/win32/fileio/hard-links-and-junctions
