#!/usr/bin/env python
from setuptools import setup, find_packages
import subprocess
import os

__doc__ = """
App for Django featuring class based email sending
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'Django>=1.4',
    'markdown',
    'PyYaml',
]

version = (0, 0, 1, 'alpha')


def get_version():
    number = '.'.join(map(str, version[:3]))
    stage = version[3]
    if stage == 'final':
        return number
    elif stage == 'alpha':
        process = subprocess.Popen('git rev-parse HEAD'.split(), stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return number + '-' + stdout.strip()[:8]

setup(
    name='django-emailtools',
    version=get_version(),
    description=__doc__,
    long_description=read('README.md'),
    packages=[package for package in find_packages() if package.startswith('emailtools')],
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
)