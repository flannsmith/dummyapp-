'''
Created on 13 Feb 2018

@author: lindasmith
'''
from setuptools import setup

setup(name="systeminfo_flask",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Linda Smith",
      author_email="linda.smithjameson@ucdconnect.ie",
      license="MIT",
      packages=['app'],
      entry_points={
          'console_scripts':['linda=app.run:main']
          }
      )

