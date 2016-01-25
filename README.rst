*************************
Cookie Cutter for Django
*************************

A Cookiecutter template for creating beautiful Django projects quickly.

Features:
========

* `Django <https://www.djangoproject.com/>`_ 1.8.X
* `Django Classy Settings <https://github.com/funkybob/django-classy-settings>`_:
  don't forget to set environment variable ``DJANGO_MODE`` (``Staging``, ``Production``)
* `Django Extensions <https://github.com/django-extensions/django-extensions>`_

Usage:
------

`Cookiecutter <https://github.com/audreyr/cookiecutter>`_ must be installed,
you can install it with pip or brew:

.. code-block:: bash

     $ pip install cookiecutter
     $ brew install cookiecutter


To create a new Django project simple do:

.. code-block:: bash

    $ cookiecutter https://github.com/pahko/cookiecutter-django.git

A promt will appear to ask you some questions about your project (project_name, etc),
simple fill those values and that's it!

TODO:
^^^^^

* include Django Rest Framework
* include base/core app
* split requirements per enviroment
* include test suite
* add support for Postgres SQL
* add tests to this template
