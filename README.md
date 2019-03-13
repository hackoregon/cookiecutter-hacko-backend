# cookiecutter-hacko-backend

A cookiecutter template for creating reusable Django REST Framework packages with the best practices quickly. This template is customized to provide structure for quickstarting a Hack Oregon civic data project.

## What is Hack Oregon?

[Hack Oregon](http://www.hackoregon.org/) is a rapid prototyping lab taking a creative approach to data projects that bring insight to complex issues in the public interest. We’re a community-powered nonprofit, our teams are made of volunteers, and all the work we do is open source.

## Features

- Tox configuration
- Sane setup.py for easy PyPI registration/distribution
- Choice of Open Source License options
- Standard templates for README, issues, Contribution guidelines

## Requirements

This repo uses the [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) templating project. You will need to install Cookiecutter. The recommended method is by a pip install:

```bash
$ pip install cookiecutter
```

## Usage

To generate a new repo:

```
$ cookiecutter gh:hackoregon/cookiecutter-hacko-backend
```

You'll be prompted for some questions, answer them, then it will create a cookiecutter-hacko-backend with your new package.

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

#### Explanation

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
