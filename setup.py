#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='yatiml',
    version='0.5.2.dev',
    description="A library for making YAML-based file formats",
    long_description=readme + '\n\n',
    author="Lourens Veen",
    author_email='l.veen@esciencecenter.nl',
    url='https://github.com/yatiml/yatiml',
    package_data={'yatiml': ['py.typed']},
    packages=[
        'yatiml',
    ],
    package_dir={'yatiml':
                 'yatiml'},
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='yatiml',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'ruamel.yaml>=0.15.71,<=0.16.10',
        'typing>=3.6; python_version<"3.5"',
        'typing_extensions'
    ],
    test_suite='tests',
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'recommonmark',
        'sphinx-rtd-theme'
    ],
    tests_require=[
        'coverage<5',
        'flake8',
        'mypy',
        'pytest>=3.5',
        'pytest-cov',
        'pycodestyle',
        'pyflakes<2.2.0',
        'pytest-flake8',
        'pytest-mypy>=0.4.0'
    ],
    extras_require={
        'dev':  ['yapf', 'isort'],
    }
)
