from setuptools import setup, find_packages
import os
import snaptiler

requirements = ['PyYAML==3.11', 'filemagic==1.6', 'Pillow==3.0.0']

setup(name='snaptiler',
	version=snaptiler.__version__,
	author='Sam Rudge',
	author_email='sam@codesam.co.uk',
	packages=find_packages(),
	install_requires=requirements,
	include_package_data=True,
    zip_safe=False,
	entry_points=""""""
	)
