#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Workspace",
    version="1.0",
    description="Python Workspace Automation",
    author="Giancarlo Rocha",
    author_email="giancarloiff@gmail.com",
    url="https://github.com/giancarlopro/workspace",
    packages=["workspace"],
    entry_points={"console_scripts": ["wsp=workspace.__main__:main"]},
)
