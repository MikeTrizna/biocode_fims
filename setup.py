#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'requests'
]

setup_requirements = [
    'pytest-runner',
    # TODO(MikeTrizna): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='biocode_fims',
    version='0.1.5',
    description="This library contains a few convenient Python functions for accessing data from the Biocode FIMS database.",
    long_description=readme + '\n\n' + history,
    author="Mike Trizna",
    author_email='mike.trizna@gmail.com',
    url='https://github.com/MikeTrizna/biocode_fims',
    packages=find_packages(include=['biocode_fims']),
    entry_points={
        'console_scripts': [
            'biocode_fims=biocode_fims.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='biocode_fims',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
