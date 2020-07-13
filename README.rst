=====
Django Inbound Rules
=====

Django Inbound Rules is an app to allow or restrict IP's group of users on specified urls based on CIDR blocks excluding user with superuser permissions.

Detailed documentation is in the "docs" directory.

Installation
-----------

    pip install django-inbound-rules

Quick start
-----------

1. Add "django-inbound" to your INSTALLED_APPS in settings.py like this::

    INSTALLED_APPS = [
        ...
        'django_inbound',
        ...
    ]

2. Add "django_inbound.middleware.restrict_user_middleware" to your MIDDLEWARE in settings.py like this::

    MIDDLEWARE = [
        ...
        'django_inbound.middleware.restrict_user_middleware',
        ...
    ]

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).


Licence
-----------
Copyright (c) 2020 Nilesh Kumar Dubey

This repository is licensed under the MIT license.
See LICENSE for details

