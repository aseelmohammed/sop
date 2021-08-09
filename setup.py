# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sop/__init__.py
from sop import __version__ as version

setup(
	name='sop',
	version=version,
	description='Standard Operating Procedure',
	author='Partner Consulting Solutions',
	author_email='aseel@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
