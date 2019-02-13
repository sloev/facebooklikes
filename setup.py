#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys
import os

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

readme = read_md('README.md')

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# get version
metadata = {}
version_filename = os.path.join(os.path.dirname(__file__), 'facebooklikes','__init__.py')
exec(open(version_filename).read(), None, metadata)

setup(
    name='facebooklikes',
    version=metadata['__version__'],
    description="Fetch facebook likes for page or facebook url",
    long_description=readme + '\n\n' + history,
    author='sloev',
    author_email=metadata['__author__'],
    url='https://github.com/sloev/facebooklikes',
    packages=[
        'facebooklikes',
    ],
    package_dir={'facebooklikes':
                 'facebooklikes'},
    include_package_data=True,
    zip_safe=False,
    keywords='facebook likes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)