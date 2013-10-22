#! /usr/bin/env python

from setuptools import setup

setup(name="apache-log-parser",
      version="1.2.0",
      author="Rory McCann",
      author_email="rory@technomancy.org",
      packages=['apache_log_parser'],
      install_requires = [
        'user-agents',
      ],
      license = 'GPLv3',
      description = "Parse lines from an apache log file",
      test_suite='apache_log_parser.tests',
)
