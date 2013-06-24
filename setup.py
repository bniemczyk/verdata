#!/usr/bin/env python

from setuptools import setup

_depends = '''
symath
'''

setup( \
  name='verdata', \
  version='git', \
  description='datastrucutres for holding versioned data in python', \
  author='Brandon Niemczyk', \
  author_email='brandon.niemczyk@gmail.com', \
  url='http://github.com/bniemczyk/verdata', \
  packages=['verdata'], \
  test_suite='tests', \
  license='BSD', \
  install_requires=_depends, \
  classifiers = [ \
    'Development Status :: 3 - Alpha', \
    'Intended Audience :: Developers', \
    'License :: OSI Approved :: BSD License' \
    ]
  )
