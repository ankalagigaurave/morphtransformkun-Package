# -*- coding: utf-8 -*-
"""setup.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vqwIzROIWBjTGRs8NiC2KFXgzV7zCpUg
"""

import setuptools
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='morphtransformkun',
      version='0.0.9',
      description='A python package for morphological transformations on image',
      url='https://github.com/ankalagigaurave/morphtransformkun-Package',
      author='Gaurav Ankalagi',
      license='MIT',
      
      packages=['morphtransformkun'],

      zip_safe=False,
      install_requires=[ 
          "opencv-python>=4.1.2",
          "numpy>=1.19.1"
      ]
      )
