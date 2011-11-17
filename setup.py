# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-qooxdoo',
    version='0.0.1',
    description='Qooxdoo integration for Django',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-qooxdoo',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    package_data={'qooxdoo': [
        'templates/*',
        'static/*',
    ]},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
