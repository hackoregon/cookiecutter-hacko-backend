=============================
{{ cookiecutter.pypi_project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://travis-ci.org/hackoregon/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/hackoregon/{{ cookiecutter.repo_name }}

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at http://hackoregon.github.io/{{ cookiecutter.repo_name }}

Quickstart
----------

Install {{ cookiecutter.pypi_project_name }}::

    pip install {{ cookiecutter.repo_name }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}.apps',
        ...
    )

Add {{ cookiecutter.pypi_project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.app_name }} import urls as {{ cookiecutter.app_name }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.app_name }}_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
