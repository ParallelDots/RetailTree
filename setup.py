from setuptools import setup, find_packages

setup(
    name="retailtree",
    version="0.0.1",
    long_description=long_description=read("README.md")
    packages=find_packages(),
    install_requires=[
        'numpy',
    ]
)
