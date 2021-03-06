#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from os.path import join, dirname

try:
    import setuptools
    setup = setuptools.setup
except ImportError:
    setuptools = None
    from distutils.core import setup

with open(join(dirname(__file__), 'qiniu', '__init__.py'), 'r') as f:
    version = re.match(r".*__version__ = '(.*?)'", f.read(), re.S).group(1)

setup(
    name='qiniu',
    version=version,
    description='Qiniu Resource Storage SDK',
    long_description='see:\nhttps://github.com/qiniu/python-sdk\n',
    author='Shanghai Qiniu Information Technologies Co., Ltd.',
    author_email='sdk@qiniu.com',
    maintainer_email='support@qiniu.com',
    license='MIT',
    url='https://github.com/qiniu/python-sdk',
    packages=['qiniu', 'qiniu.services', 'qiniu.services.storage', 'qiniu.services.processing'],
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['requests'],

    entry_points={
        'console_scripts': [
            'qiniupy = qiniu.main:main',
        ],
    }
)
