# setup.py
from setuptools import setup, find_packages

setup(
    name="alluuid",
    version="0.1.2",
    author="Krishna Tadi",
    description="AllUUID is a versatile Python library and cli tool for generating universally unique identifiers (UUIDs). It supports multiple versions of UUIDs, including version 1 (time-based), version 4 (random), and version 7 (timestamp-based). Features an easy-to-use CLI for UUID generation. This tool is ideal for developers looking to create unique identifiers for databases, session tokens, or any other use cases where uniqueness is critical.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krishnatadi/alluuid-pypi",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "alluuid=alluuid.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/krishnatadi/alluuid-pypi/issues",
        "Source Code": "https://github.com/krishnatadi/alluuid-pypi",
    },
    python_requires=">=3.6",
)
