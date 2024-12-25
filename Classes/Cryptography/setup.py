#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build and install the TweetNaCl wrapper, modified for Squad Busters/other new Supercell Games.
"""

from __future__ import print_function

import platform
from setuptools import setup, Extension  # Use setuptools instead of distutils

# Define libraries to link against
libraries = []

if platform.system() == "Windows":
    libraries.append("advapi32")

# Define the Extension object
nacl_module = Extension(
    '_tweetnaclSquad',
    sources=["tweetnaclmodule.c", "tweetnacl.c", "randombytes.c"],
    libraries=libraries,
    extra_compile_args=["-O2", "-funroll-loops", "-fomit-frame-pointer"]
)

# Define the setup configuration
setup(
    name='tweetnaclSquad',
    version='0.2',
    author="Brian Warner, Jan Mojžíš",
    description="Python wrapper for TweetNaCl",
    ext_modules=[nacl_module],  # Extensions to compile
    packages=["nacl"],  # Package name
    package_dir={"nacl": ""},  # Directory for the 'nacl' package
)
