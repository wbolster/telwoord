Telwoord
========

A Python library to convert numbers into their Dutch (nl) written form.


Installation
============

To install from a source tree::

    $ pip install -e .

Eventually this will become::

    $ pip install telwoord

There are no dependencies; a Python 2 or Python 3 interpreter is all you need.


Usage
=====

Use ``telwoord.cardinal()`` to convert an integer to its string representation.

By default, a friendly representation is used, based on some common style
recommendations::

    >>> from telwoord import cardinal

    >>> numbers = (0, 1, 2, 3, 19, 20, 30, 31, 100, 200, 215, 300, 14999, 15000, 1000000, 12345678)

    >>> [cardinal(n) for n in numbers]
    ['nul', 'een', 'twee', 'drie', 'negentien', 'twintig', 'dertig', '31', 'honderd', 'tweehonderd', '215', 'driehonderd', '14999', '15 duizend', '1 miljoen', '12345678']

If you are not in a friendly mood though, you can forcibly spell out all the
numbers as well::

    >>> [cardinal(n, friendly=False) for n in numbers]
    ['nul', 'een', 'twee', 'drie', 'negentien', 'twintig', 'dertig', 'eenendertig', 'honderd', 'tweehonderd', 'tweehonderdvijftien', 'driehonderd', 'veertienduizend negenhonderdnegenennegentig', 'vijftienduizend', 'een miljoen', 'twaalf miljoen driehonderdvijfenveertigduizend zeshonderdachtenzeventig']


Rules and style recommendations
===============================

* Taalunie, `Aaneenschrijven van telwoorden
  <http://woordenlijst.org/leidraad/6/9/>`_

* Genootschap Onze Taal, `Getallen in letters of cijfers
  <https://onzetaal.nl/taaladvies/advies/getallen-in-letters-of-cijfers>`_

* Genootschap Onze Taal, `Getallen uitschrijven
  <https://onzetaal.nl/taaladvies/advies/getallen-uitschrijven>`_


Development
===========

To run the tests::

    $ py.test

Possible future work:

* Ordinal numbers
* Fractions
