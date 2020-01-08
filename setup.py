from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='unweb.trusted',
      version=version,
      description="Trusted users extension for the listen mailing list system",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['unweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [topp.zcmlloader]
      opencore = unweb.trusted

      [z3c.autoinclude.plugin]
      target = plone
      """,
      #setup_requires=["Paste==1.7.5.1", "PasteScript==1.7.5"],
      #paster_plugins=["ZopeSkel"],
      )
