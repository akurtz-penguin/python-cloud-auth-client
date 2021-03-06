import os
import sys

from setuptools import setup, find_packages

requires = [
    'requests',
    'oauth2'
    ]

pyversion = sys.version_info[:2]
if pyversion < (2, 6):
    requires.append('simplejson')

setup(
    name="python-cloud-auth-client",
    version="0.1.1",
    description="Client library for Scyld Cloud Auth API",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent"
    ],
    author="Penguin Computing, Inc.",
    maintainer="Penguin Computing, Inc.",
    maintainer_email="support@penguincomputing.com",
    url="http://www.penguincomputing.com",
    packages=find_packages(exclude=['tests','tests.*']),
    install_requires=requires
)
