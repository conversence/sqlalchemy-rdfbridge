from setuptools import setup, find_packages
import os

version = '0.1'


def readme():
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, "README.md")
    return open(filename).read()


setup(name='sqlalchemy-rdfbridge',
      version=version,
      description="Define and collect RDF mapping information in SQLAlchemy schemas",
      long_description=readme(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords='',
      author='Marc-Antoine Parent',
      author_email='maparent@acm.org',
      url='https://github.com/maparent/sqlalchemy-rdfbridge',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      tests_require=["pytest"],
      requires=[
          'SQLAlchemy',
          'rdflib'
      ],
      )
