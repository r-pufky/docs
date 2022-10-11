.. _wbase-specific-windows-fixes-ntfs-file-ownership-access-denied:

NTFS File Ownership Access Denied
#################################
When reinstalling windows, or moving a drive to another system, sometimes the
NTFS file system will deny access to files you own. This is generally because
the default well known SIDs were removed from the file permissions, and
replaced with a specific user SID that no longer exists (and now can no longer
be removed, prompting this perms error everytime you access it). You can fix
this by replacing the old SID with the new SID:

.. code-block:: powershell
  :caption: Replace old SID with current system SID (powershell as admin).

  setacl.exe -on c:\ -ot file -actn trustee -trst "n1:S-old-501;n2:S-new-501;ta:repltrst" -rec cont

Alternatively take ownership and copy files to a NTFS partition with proper
SID's set.

The affected NTFS partition should really be nuked and re-formatted using well
known SIDs which will remove this issue.

`Reference <https://superuser.com/questions/439675/how-to-bind-old-users-sid-to-new-user-to-remain-ntfs-file-ownership-and-permiss>`__

`Reference <https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows>`__
