# cookiecutter-hacko-backend

[![Build Status](https://travis-ci.org/hackoregon/cookiecutter-hacko-backend.svg?branch=master)](https://travis-ci.org/hackoregon/cookiecutter-hacko-backend)

A cookiecutter template for creating reusable Django REST Framework packages with the best practices quickly. This template is customized to provide structure for quickstarting a Hack Oregon civic data project.

## What is Hack Oregon?

[Hack Oregon](http://www.hackoregon.org/) is a rapid prototyping lab taking a creative approach to data projects that bring insight to complex issues in the public interest. We’re a community-powered nonprofit, our teams are made of volunteers, and all the work we do is open source.

## Features

- Tox configuration
- Sane setup.py for easy PyPI registration/distribution
- Choice of Open Source License options
- Standard templates for README, issues and pull requests, Contribution guidelines

## Requirements

This repo uses the [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) templating project. You will need to install Cookiecutter. The recommended method is by a pip install:

```bash
$ pip install cookiecutter
```

## Usage

To generate a new repo:

```
$ cookiecutter gh:hackoregon/cookiecutter-hacko-backend --checkout BRANCH
```

You can leave out the `--checkout BRANCH` if checking out from MASTER.

You'll be prompted for some questions, answer them, then it will create a cookiecutter-hacko-backend with your new package.

At this point, you are ready to connect with an external git.

### Cookiecutter values

You will be asked the following information when creating a project:

```
{
  "full_name": "Your full name here",
  "email": "you@example.com",
  "github_username": "yourname",
  "pypi_project_name": "djangorestframework-package",
  "repo_name": "django-rest-framework-package",
  "app_name": "rest_framework_package",
  "project_short_description": "Your project description goes in here",
  "year": "2015",
  "version": "0.1.0",
  "open_source_license": ["MIT", "BSD", "ISCL", "Apache Software License 2.0", "Not open source"]
}
```

### Explanation

- full_name: Your name as project originator (for credit in documentation)
- email: Your email address
- github_username: Your github username
- pypi_project_name: Cannonical name which will be used within package registry
- repo_name: Master project repository name on github
- app_name: Name of the Django Rest Framework package (what will be imported to project)
- project_short_description: A brief description of the project
- year: current year project is created
- version: initial version of the app, should be 0.1.0 if new project
- open_source_license: Type of License to apply

### Example

## Tests

To run tests on the Cookiecutter generation, please install TOX, which is a generic virtualenv management and test command line tool.

TOX is avaiable to install from PyPI via pip:

```
$ pip install tox
```

It will automatically create a fresh virtual environment and install our test dependencies,
such as `pytest-cookies` and `flake8`.

## Run the Tests

Tox uses py.test under the hood, hence it supports the same syntax for selecting tests.

For further information please consult the `pytest usage docs`.

To run all tests using various versions of python in `virtualenvs` defined in `tox.ini`, just run tox:

```
    $ tox
```

It is possible to test with a specific version of python. To do this, the command
is:

```
    $ tox -e py36
```

This will run py.test with the python3.6 interpreter, for example.

To run a particular test with tox for against your current Python version:

```
    $ tox -e py -- -k test_default_configuration
```

* [pytest usage docs](https://pytest.org/latest/usage.html#specifying-tests-selecting-tests)
* [tox](https://tox.readthedocs.io/en/latest/)
* [pip](https://pypi.python.org/pypi/pip/)
* [pytest-cookies](https://pypi.python.org/pypi/pytest-cookies/)
* [flake8](https://pypi.python.org/pypi/flake8/)
* [PyPI](https://pypi.python.org/pypi)
