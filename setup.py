from setuptools import setup, find_packages
import tilepaper

requirements = ['PyYAML==3.11', 'filemagic==1.6', 'Pillow==3.0.0']

setup(name='tilepaper',
      version=tilepaper.__version__,
      author='Sam Rudge',
      author_email='sam@codesam.co.uk',
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      zip_safe=False,
      url="https://github.com/samarudge/tilepaper",
      entry_points="""
[console_scripts]
tilepaper = tilepaper.cli:run
""",
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Utilities'
      ]
      )
