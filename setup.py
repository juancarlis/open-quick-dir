from setuptools import setup


setup(
    name="oqd",
    version="0.1",
    py_modules=["odq"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        oqd=oqd:cli
    """,
)
