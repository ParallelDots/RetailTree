from setuptools import setup, find_packages

def read( fname ):
    with open(fname) as fp:
        content = fp.read()
    return content
    
setup(
    name="retailtree",
    version="1.1",
    long_description=read("Desc.rst"),
    packages=find_packages(),
    install_requires=[
        'numpy',
    ]
)
