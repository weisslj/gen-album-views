#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='gen-album-views',
      version='1.0',
      description='Generate additional indices of a well structured music collection via hardlinks.',
      author=u'Johannes Weißl',
      author_email='jargon@molb.org',
      url='http://github.com/weisslj/gen-album-views',
      license='GNU GPL v3',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python :: 2.5',
          'Topic :: Utilities',
      ],
      scripts=['gen-album-views'])
