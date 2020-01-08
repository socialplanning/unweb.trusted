from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='unweb.trusted',
      version=version,
      description="Trusted users extension for the listen mailing list system",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications :: Email",
        "Topic :: Communications :: Email :: Email Clients (MUA)",
        "Topic :: Communications :: Email :: Mailing List Servers",
        "Topic :: Communications :: Email :: Mail Transport Agents",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='trusted users opencore listen mailing list system',
      author='',
      author_email='',
      url='https://github.com/socialplanning/unweb.trusted/',
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
