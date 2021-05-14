#!/usr/bin/env python3

import setuptools

import funcpipes
long_description = funcpipes.__doc__

setuptools.setup(
    name='a_kvnl',
    version='0.1.0',
    author='Mihail Georgiev',
    author_email='misho88@gmail.com',
    description='Annotations/KVNL',
    long_description=long_description,
    long_description_content_type='text/plain',
    url='https://github.com/misho88/a-kvnl',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    py_modules=['a_kvnl']
)
