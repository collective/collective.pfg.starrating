# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os

version = '1.0'

shortdesc = 'Star Rating Field for PloneFormGen'
_basepath = os.path.dirname(__file__)
longdesc = open(os.path.join(_basepath, 'README.rst')).read()
longdesc += open(os.path.join(_basepath, 'CHANGES.rst')).read()
longdesc += open(os.path.join(_basepath, 'LICENSE.rst')).read()

setup(
    name='collective.pfg.starrating',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Framework :: Plone',
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'Products.PloneFormGen',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
