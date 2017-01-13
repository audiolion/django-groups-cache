.. :changelog:

History
-------

0.5.5 (2017-01-13)
++++++++++++++++++

* Bug fix for templatetag `has_group`
* Tests added for 100% coverage of templatetag folder

0.5.5 (2017-01-12)
++++++++++++++++++

* Omit urls.py from coverage report (not used but needed for django package)
* Omit apps.py from coverage report (default apps file)

0.5.4 (2017-01-12)
++++++++++++++++++

* Removal of py32/django1.8 support from Travis CI build

0.5.3 (2017-01-12)
++++++++++++++++++

* Fixing .travis.yml file and CI builds

0.5.2 (2017-01-12)
++++++++++++++++++

* Typo in README.rst

0.5.1 (2017-01-12)
++++++++++++++++++

* Add codecov.io support
* Documentation updates

0.5.0 (2017-01-12)
++++++++++++++++++

* Add requirements.txt to tox.ini so tests can run
* Fix broken compatibility with Django 1.8/1.9 due to backwards incompatible changes in 1.9/1.10 code

0.4.0 (2017-01-12)
++++++++++++++++++

* Add test suite that generates 100% coverage
* Fixed a bug found by test suite with cache not invalidating on the `groups` ManyToManyField changing

0.3.1 (2017-01-11)
++++++++++++++++++

* Documentation updates

0.3.0 (2017-01-11)
++++++++++++++++++

* First stable and working release on PyPI.

0.1.0 (2017-01-11)
++++++++++++++++++

* First release on PyPI.
