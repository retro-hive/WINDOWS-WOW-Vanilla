#!/usr/bin/env python
# encoding: UTF-8

import os
from setuptools import setup, find_packages

long_description = ""

try:
    if os.path.isfile("README.rst"):
        long_description = open("README.rst", "r").read()
except Exception as error:
    print("Unable to read the README file: " + str(error))


setup(
    name="WINDOWS-WOW-Vanilla",
    version="0.0.0",
    description="World of Warcraft - Vanilla",
    url="https://github.com/retro-hive/WINDOWS-WOW-Vanilla",
    license="WTFPL",

    long_description=long_description,

    author="Guillaume FRILOUX",

    keywords="WoW Vanilla eBook",
    platforms=["Linux", "Windows"],

    packages=find_packages(),

    install_requires=[
        "setuptools",
    ],

    extras_require={
        "dev": [
            "Sphinx",
            "sphinx-rtd-theme",
            "nox",
            "black",
        ],
    },

    # cmdclass={"install": install}
)
