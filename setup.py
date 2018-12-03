#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:17:10 2018

@author: SaintlyVi
"""
from setuptools import setup, find_packages

setup(
      name='dlr_data_retrieval',
      version=0.1,
      description='Fetches data from a DLR MSSQL database',
      long_description='This module helps researchers with limited\
      SQL knowledge to extract data from the Domestic Load Research\
      database and store it on disk in a directory structure for local\
      processing.',
      keywords='domestic load research south africa data access',
      url='https://github.com/wiebket/dlr_data_retrieval',
      author='Wiebke Toussaint',
      author_email='wiebke.toussaint@gmail.com',
      packages=find_packages(),
      license='CC-BY-NC',
      install_requires=['pandas','numpy','pyodbc','feather','os','glob','plotly', 
                        'optparse', 'pathlib'],
      include_package_data=True,
      entry_points = {
			'console_scripts': ['retrieve_dlr=src.command_line:main'],
    		}
      )
