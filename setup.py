from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="SloPOS",
      version="1.1",
      description="Part of speech tagger for Slovenian (SI) language based on NLTK",
      package_data={'slopos': ["sl-tagger.pickle"]},
      license="LGPL",
      url="https://github.com/izacus/slo_pos",
      author="Jernej Virag",
      author_email="jernej@virag.si",
      classifiers=[
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: OS Independent",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Topic :: Text Processing :: Linguistic"
      ],
      install_requires=["nltk"],
      long_description=long_description,
      long_description_content_type='text/markdown'
      packages=["slopos"])

