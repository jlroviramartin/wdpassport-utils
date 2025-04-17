
from setuptools import setup

setup(name='wdpassport_utils',
      version='0.2',
      description='WD My Passport Drive Hardware Encryption Utility for Linux',
      url='https://github.com/jlroviramartin/wdpassport-utils',
      author='0-duke, crypto-universe, JoshData, jlroviramartin',
      author_email='jt@occams.info',
      license='GPLv2',
      install_requires=[
        'pyudev',
        'py3_sg @ git+https://github.com/jlroviramartin/py3_sg',
      ],
      scripts=['wdpassport-utils.py'],
      )
