"""
Setup file for installing package.
"""

from os import path
from setuptools import setup, find_packages

__version__ = '0.1.0'

HERE = path.abspath(path.dirname(__file__))

LONG_DESCRIPTION = """`markovclick` allows you to model clickstream data from\
websites as Markov chains, which can then be used to predict the next likely\
click on a website for a user, given their history and current state.
"""

setup(
    name='markovclick',
    version=__version__,
    description='Package for modelling clickstream data using Markov chains',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/ismailuddin/markovclick',
    download_url='https://github.com/ismailuddin/markovclick/tarball/' + __version__,
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Ismail Uddin',
    # install_requires=INSTALL_REQUIRES,
    # dependency_links=DEPENDENCY_LINKS,
)
