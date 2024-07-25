========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/pyCRDTs/badge/?style=flat
    :target: https://readthedocs.org/projects/pyCRDTs/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/Adrien-LUDWIG/pyCRDTs/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/Adrien-LUDWIG/pyCRDTs/actions

.. |codecov| image:: https://codecov.io/gh/Adrien-LUDWIG/pyCRDTs/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/Adrien-LUDWIG/pyCRDTs

.. |version| image:: https://img.shields.io/pypi/v/pycrdts.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/pycrdts

.. |wheel| image:: https://img.shields.io/pypi/wheel/pycrdts.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/pycrdts

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycrdts.svg
    :alt: Supported versions
    :target: https://pypi.org/project/pycrdts

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pycrdts.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/pycrdts

.. |commits-since| image:: https://img.shields.io/github/commits-since/Adrien-LUDWIG/pyCRDTs/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/Adrien-LUDWIG/pyCRDTs/compare/v0.0.0...main



.. end-badges

A CRDT library in Python.

* Free software: MIT license

Installation
============

::

    pip install pycrdts

You can also install the in-development version with::

    pip install https://github.com/Adrien-LUDWIG/pyCRDTs/archive/main.zip


Documentation
=============


https://pyCRDTs.readthedocs.io/


Development
===========

To run all the tests run::

    tox

To run only the tests for a specific environment run, e.g. for Python 3.12 with coverage::

    tox -e py312-cover

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
