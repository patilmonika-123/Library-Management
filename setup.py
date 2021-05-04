# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in library_mgnt/__init__.py
from library_mgnt import __version__ as version

setup(
	name='library_mgnt',
	version=version,
	description='Library Management System',
	author='Monika Patil',
	author_email='monika.p@indictrans.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
