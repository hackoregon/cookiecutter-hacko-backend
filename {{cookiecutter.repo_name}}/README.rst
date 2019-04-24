=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.project_slug }}

.. image:: https://travis-ci.org/hackoregon/{{ cookiecutter.project_slug }}.svg?branch=master
    :target: https://travis-ci.org/hackoregon/{{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at http://hackoregon.github.io/{{ cookiecutter.project_slug }}

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.project_slug }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.project_slug }}.apps',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.project_slug }} import urls as {{ cookiecutter.project_slug }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.project_slug }}_urls)),
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
