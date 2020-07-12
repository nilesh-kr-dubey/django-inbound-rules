=====
Django Inbound Rules
=====

Django Inbound Rules is an app to allow or restrict IP's on specified urls based on CIDR blocks.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django-inbound" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_inbound',
        ...
    ]

2. Add "django_inbound.middleware.restrict_user_middleware" to your MIDDLEWARE setting like this::

    MIDDLEWARE = [
        ...
        'django_inbound.middleware.restrict_user_middleware',
        ...
    ]

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

