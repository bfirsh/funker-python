#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='funker',
    version='0.0.1',
    description='Functions as Docker containers',
    url='https://github.com/bfirsh/funker-python',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={},
    install_requires=[
        'six',
    ],
    include_package_data=True,
)
