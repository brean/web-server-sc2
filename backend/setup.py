#!/usr/bin/env python3
import os
from setuptools import find_packages, setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sc2_websocket_bridge",
    description="StarCraft II WebSocket Bridge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/web-server-sc2",
    version="0.1",
    license="BSD-3",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=[],
    include_package_data=True,
    install_requires=[
        'argcomplete',
        'fastapi',
        'pyyaml',
        'uvicorn',
        'websockets'
    ],
    entry_points={
        'console_scripts': [
            'sc2_web = sc2_websocket_bridge.cli:main',
        ],
    },
)
