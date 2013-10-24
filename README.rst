Telwoord
========

A Python library to convert numbers into their Dutch written form.


Installation
============

To install from a source tree::

    $ pip install -e .

Eventually this will become::

    $ pip install telwoord


Dependencies
============

No dependencies; a Python 2 or Python 3 interpreter is all you need.


Development status
==================

This is a work in progress and should be considered alpha quality software.


Usage
=====

Convert an integer to a (Unicode) string using the ``telwoord.cardinal()``
function::

    from telwoord import cardinal

    # This prints "een", "tweeëntwintig", "tweeëntwintighonderd",
    # "tweeduizend tweehonderdtwintig", "nul", and "min twaalf"

    for n in (1, 22, 2200, 2220, 0, -12):
        print(cardinal(n))

You can specify an optional `threshold` argument, as required by some style
guides::

    cardinal(n, threshold=7)  # returns "13", not "dertien"


Grammatical and spelling rules
==============================

* Taalunie, `Aaneenschrijven van telwoorden
  <http://woordenlijst.org/leidraad/6/9/>`_

* Genootschap Onze Taal, `Getallen in letters of cijfers
  <https://onzetaal.nl/taaladvies/advies/getallen-in-letters-of-cijfers>`_

* Genootschap Onze Taal, `Getallen uitschrijven
  <https://onzetaal.nl/taaladvies/advies/getallen-uitschrijven>`_


Possible future work
====================

* Ordinal numbers

* Fractions


Development
===========

To run the tests::

    $ py.test
