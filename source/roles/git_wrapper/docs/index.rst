.. _service-gitea:

Gitea
#####
A community managed fork of gogs. This provides a github-like service for
private repository use. Can be exposed and used publicly.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration
   repositories
   troubleshooting

.. role:: do1jlr.gitea
  :galaxy:       https://galaxy.ansible.com/do1jlr/gitea
  :source:       https://github.com/roles-ansible/ansible_role_gitea
  :service_doc:  https://docs.gitea.io/en-us/
  :ref:          https://github.com/go-gitea/gitea,
                 https://docs.gitea.io/en-us/config-cheat-sheet/
  :update:       2022-10-08
  :open:

  * Though there is some documentation on moving from ``sqlite3`` to
    ``postgresql`` for gitea; all migrations seem to carry over artifacts that
    express different kinds of failures (like 500's on issue updates). Decide
    on a backend **before committing** any amount of metadata to Gitea.
  * See :ref:`service-gitea-basic-configuration` for example configuration.

  ..  collapse:: README.md

    .. literalinclude:: source/README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml
