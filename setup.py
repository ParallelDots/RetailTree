from setuptools import setup, find_packages

def read( fname ):
    with open(fname) as fp:
        content = fp.read()
    return content
    
setup(
    name="retailtree",
    version="0.0.1",
    long_description=read("description.rst"),
    packages=find_packages(),
    install_requires=[
        'numpy',
    ]
)
