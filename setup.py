from setuptools import setup


setup(
    name="oqd",
    version="0.1",
    py_modules=["oqd"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        oqd=src.oqd:cli
    """,
)
