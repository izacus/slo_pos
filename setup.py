from distutils.core import setup

setup(name="SloPOS",
      version="1.0",
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
          "Topic :: Text Processing :: Linguistic"
      ],
      install_requires=["nltk"],
      packages=["slopos"])

