:github_url: https://github.com/LizardByte/RetroArcher-plex/tree/nightly/docs/source/contributing/build.rst

Build
=====
Compiling RetroArcher-plex is fairly simple; however it is recommended to use Python 2.7 since the Plex framework is using
Python 2.7.

Clone
-----
Ensure `git <https://git-scm.com/>`_ is installed and run the following:

   .. code-block:: bash

      git clone https://github.com/lizardbyte/retroarcher-plex.git retroarcher-plex.bundle
      cd ./retroarcher-plex.bundle

Setup venv
----------
It is recommended to setup and activate a `venv`_.

Install Requirements
--------------------
Install Requirements
   .. code-block:: bash

      # use python 2.7 venv
      python ./scripts/install_requirements.txt

Development Requirements
   .. code-block:: bash

      python -m pip install -r ./scripts/requirements-dev.txt

Build Plist
-----------
   .. code-block:: bash

      python ./scripts/build_plist.py

Remote Build
------------
It may be beneficial to build remotely in some cases. This will enable easier building on different operating systems.

#. Fork the project
#. Activate workflows
#. Trigger the `CI` workflow manually
#. Download the artifacts from the workflow run summary

.. _venv: https://docs.python.org/3/library/venv.html
