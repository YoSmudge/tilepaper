from setuptools import setup, find_packages
import tilepaper

requirements = ['PyYAML==3.11', 'filemagic==1.6', 'Pillow==3.0.0']

setup(name='tilepaper',
      version=tilepaper.__version__,
      author='Sam Rudge',
      author_email='sam@codesam.co.uk',
      description='Generate OS/X "Shifting Tiles" style wallpapers',
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      zip_safe=False,
      url="https://www.codedog.co.uk/tilepaper",
      licence="MIT",
      entry_points="""
[console_scripts]
tilepaper = tilepaper.cli:run
""",
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ]
      )
