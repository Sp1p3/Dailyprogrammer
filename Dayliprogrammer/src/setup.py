__author__ = "canillas"
__date__ = "$5 f�vr. 2015 10:50:54$"

from setuptools import setup, find_packages

setup (
       name='Dayliprogrammer',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='canillas',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )