# Django Inbound Rules

## Description
Django Inbound Rules is an app to allow or restrict group of users on specified url(s) based on CIDR blocks(now IPv4 only) excluding user with superuser permissions.

## Installation
```pip install django-inbound-rules```

## Quick start

1. Add "inbound" to your INSTALLED_APPS in settings.py like this::

    ```
    INSTALLED_APPS = [
        ...
        'inbound',
        ...
    ]
    ```

2. Add "inbound.middleware.restrict_user_middleware" to your MIDDLEWARE in settings.py like this::

    ```
    MIDDLEWARE = [
        ...
        'inbound.middleware.restrict_user_middleware',
        ...
    ]
    ```

3. Run ```python manage.py migrate``` to implement django-inbound-rules.

4. Start the development server and visit ```http://127.0.0.1:8000/admin/``` to create your Inbound Rules.

5. For working logic, see documentation.


## Licence
Copyright (c) 2020 Nilesh Kumar Dubey

This repository is licensed under the MIT license.
See LICENSE for details
