# Django Inbound Rules

## Description
Simple Paginator for Djnago templates

## Installation
```pip install django-inbound-rules```

## Quick start

1. Add "django-inbound" to your INSTALLED_APPS in settings.py like this::

    ```
    INSTALLED_APPS = [
        ...
        'django_inbound',
        ...
    ]
    ```

2. Add "django_inbound.middleware.restrict_user_middleware" to your MIDDLEWARE in settings.py like this::

    ```
    MIDDLEWARE = [
        ...
        'django_inbound.middleware.restrict_user_middleware',
        ...
    ]
    ```

3. Run ```python manage.py migrate``` to create the inbound rules models.


## Licence
Copyright (c) 2020 Nilesh Kumar Dubey

This repository is licensed under the MIT license.
See LICENSE for details
