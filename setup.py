from setuptools import setup
from pathlib import Path


setup(
    name="oqd",
    version="0.1",
    packages=["src", "src.dirs", "src.navigation"],
    py_modules=["src.oqd"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        oqd=src.oqd:cli
    """,
)
