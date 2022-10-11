.. _service-gitea-repository-management:

Repository Management
#####################

Importing Git Repositories
**************************
You can import other git repositories, including local and cloned ones:

* Create an aptly named repository on Gitea, intialize it empty.
* Push a mirror to this repository. All information will be retained.
* Disable SSL verification if using self-signed certs.

.. code-block:: bash
  :caption: Push mirror to Gitea.

  cd my-repo-to-import
  git push --mirror https://{IP}:3000/{USER}/{REPO}.git

As this is a mirror, you want to commit the *git metadata* and not just the
files. The git repository is stored in ``gitea_repository_root`` as a standard
git repository. Importing this way sets up the Gitea frontend database metadata
for the project.

`Reference <https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server>`__

`Reference <https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate>`__

Mirrors
*******
Gitea mirrors can automaticallly manage upstream mirror syncs if setup to do
so. This will also allow for local forking of those mirrors for indiviudal use.

.. gui::   Create Mirror
  :path:   + --> New Migration
  :value0: Migrate / Clone from URL, {REMOTE REPOSITORY URL}
  :value1: Owner, {ORGANIZATION OWNER}
  :value2: Repository Name, {SAME REPO NAME}
  :value3: Visibility, ☑ Make Repository Private
  :value4: Migration Type, ☑ This repository will be a mirror
  :value5: Description, {DESCRIPTION}

`Reference <https://github.com/go-gitea/gitea/issues/4493>`__
