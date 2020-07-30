
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="django-inbound-rules",
    version="1.0.0",
    description="Django Inbound Rules is an app to allow or restrict group of users on specified url(s) based on CIDR blocks(now IPv4 only) excluding user with superuser permissions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nilesh-kr-dubey/django-inbound-rules",
    author="Nilesh Kumar Dubey",
    author_email="nileshdubeyindia@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=['inbound'],
    install_requires=[
        "Django >= 2.0",
    ],
    include_package_data=True,
    project_urls={
        'Documentation': 'https://github.com/nilesh-kr-dubey/django-inbound-rules/tree/master/docs',
    },
)
