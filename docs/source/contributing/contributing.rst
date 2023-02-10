:github_url: https://github.com/LizardByte/RetroArcher-plex/tree/nightly/docs/source/contributing/contributing.rst

Contributing
============
#. Fork the repo on GitHub
#. Follow the instructions in :ref:`Build <contributing/build:build>` as required, replacing the .git url with your
   fork's url.
#. Create a new branch for the feature you are adding or the issue you are fixing

   .. Tip:: Base the new branch off the `nightly` branch. It will make your life easier when you submit the PR!

#. Make changes, push commits, etc.
#. Follow `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_.
#. Files should contain an empty line at the end.
#. Document your code!
#. :ref:`Test <contributing/testing:testing>` your code!
#. When ready create a PR to this repo on the `nightly` branch.

   .. Hint:: If you accidentally make your PR against a different branch, a bot will comment letting you know it's on
      the wrong branch. Don't worry. You can edit the PR to change the target branch. There is no reason to close the
      PR!

   .. Note:: Draft PRs are also welcome as you work through issues. The benefit of creating a draft PR is that an
      automated build can run in a github runner.

   .. Attention:: Do not expect partially complete PRs to be merged. These topics will be considered before merging.

      - Does the code follows the style guidelines of this project?

         .. Tip:: Look at examples of existing code in the project!

      - Is the code well commented?
      - Were docstrings updated for new or modified methods?
      - Were tests added for new methods?
      - Were tests adjusted for modified methods?

   .. Note:: Developers and maintainers will attempt to assist with challenging issues. For example, perhaps you want
      to merge a feature and know how to add the feature but not test it. We will help with that!
