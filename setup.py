#!/usr/bin/env python

from distutils.core import setup

setup(name='ModestMaps',
      version='1.2.1',
      description='Modest Maps python port',
      author='Michal Migurski',
      url='http://modestmaps.com',
      requires=['PIL'],
      packages=['ModestMaps', 'wscompose'],
      scripts=['ws-compose.py', 'ws-pinwin.py', 'compose.py'],
      download_url='http://modestmaps.com/dist/ModestMaps-Py-1.2.0.tar.gz',
      license='BSD')
