============
Contributing
============

The best way to contribute to this project is by `volunteering <http://www.hackoregon.org/>`_ with Hack Oregon during a project season.

Hack Oregon is a rapid prototyping lab taking a creative approach to data projects that bring insight to complex issues in the public interest. We’re a community-powered nonprofit, our teams are made of volunteers, and all the work we do is open source.

We do allow for limited individual contributions from users outside our organization. We would first ask that you review our `Code of Conduct <http://www.hackoregon.org/code-of-conduct/>`_

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/{{ hackoregon }}/{{ cookiecutter.repo_name }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.pypi_project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.pypi_project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/hackoregon/{{ cookiecutter.repo_name }}/issues.

Implement Features
~~~~~~~~~~~~~~~~~~

Feature adoption will be limited in scope to the project goals and mission of Hack Oregon and it's parent organization the Civic Software Foundation.

If you are not actively involved in a Hack Oregon team, please open an issue prior to beginning to work on any new features.

For Hack Oregon Team Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are proposing a feature:

* Open a new github issue for an Enhancement Request.
* Explain in detail how it would work.
* Explain how this feature relates to your project scope. Including links to any related cards.
* Keep the scope as narrow as possible, to make it easier to implement.

Get Started!
------------

Ready to contribute? Here's how to set up `{{ cookiecutter.repo_name }}` for local development.


For Hack Oregon Team Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(If you are a public contributor See This)

1. Confirm your Github username is part of the Hack Oregon Organization, and you are a contributor on on the `{{ cookiecutter.repo_name }}` repository.

2. Clone locally::

    $ git clone https://github.com/hackoregon/{{ cookiecutter.repo_name }}.git

3. Install your local copy in either a virtualenv or a docker container::

    $ cd {{ cookiecutter.repo_name }}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

        $ flake8 {{ cookiecutter.app_name }} tests
        $ python setup.py test
        $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. Update HISTORY.rst with your changes under the date and version tag
3. The pull request should work for <Which python versions? 3.X stable only?>. Check
   https://travis-ci.org/hackoregon/{{ cookiecutter.repo_name }}/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

    $ python -m unittest tests.test_{{ cookiecutter.app_name }}
