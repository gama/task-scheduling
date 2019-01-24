#!/usr/bin/env python
# pylama:ignore=E221,E251

from setuptools import find_packages, setup

setup(
    name         = 'task_scheduling',
    version      = '1.0',
    description  = 'Cerebras Task Scheduling Exercise',
    author       = 'Gustavo Gama',
    author_email = 'gustavo.gama@gmail.com',
    url          = 'https://gama.igenesis.com.br',
    packages     = find_packages()
)
