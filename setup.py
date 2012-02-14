from os.path import exists
from distutils.core import setup
from liveserver import __version__

setup(
    name='django-live-server',
    version=__version__,
    # Your name & email here
    maintainer='Adam Charnock',
    maintainer_email='adam@playnice.ly',
    # If you had liveserver.tests, you would also include that in this list
    packages=['liveserver'],
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    # REQUIRED: Your project's URL
    url='https://github.com/adamcharnock/django-live-server',
    license='BSD',
    description='Implementation of the LiveServerTestCase code due out in Django 1.4',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[
        "django<1.4",
    ],
)
