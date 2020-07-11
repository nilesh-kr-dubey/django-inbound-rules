# Django Inbound Rules

## Description
Django Inbound Rules is an app to allow or restrict IP's on specified urls based on CIDR blocks. Detailed documentation is in the "docs" directory.

## Installation
```pip install django-inbound-rules```

## Quick start

1. Add "django-inbound" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...
        'django_inbound',
    ]
    ```

2. Add "django_inbound.middleware.restrict_user_middleware" to your MIDDLEWARE setting like this::

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
