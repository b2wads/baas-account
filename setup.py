from codecs import open  # To use a consistent encoding
from os import path

from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

setup(
    name="baas-account",
    version="0.1.0",
    description="Banco as a Service - Account",
    long_description="",
    url="https://github.com/b2wdigital/baas-account",
    # Author details
    author="Dalton Matos",
    author_email="daltonmatos@b2wdigital.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)
