
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="django-inbound-rules",
    version="0.1",
    description="Django Inbound Rules is an app to allow or restrict IP's on specified urls based on CIDR blocks.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nilesh-kr-dubey/django-inbound-rules",
    author="Nilesh Kumar Dubey",
    author_email="nileshdubeyindia@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    include_package_data=True,
)
