Telwoord
========

A Python library to convert numbers into their Dutch (nl) written form.

.. image:: https://travis-ci.org/wbolster/telwoord.png?branch=master
   :target: https://travis-ci.org/wbolster/telwoord

Links:

* Code: https://github.com/wbolster/telwoord
* PyPI: https://pypi.python.org/pypi/telwoord
* Travis CI: https://travis-ci.org/wbolster/telwoord

Installation
============


To install from PyPI::

    $ pip install telwoord

There are no dependencies; a Python 2 or Python 3 interpreter is all you need.


Usage
=====

Use ``telwoord.cardinal()`` to convert an integer to its string representation.

By default, a friendly representation is used, based on some common style
recommendations about when to spell out numbers, and when to leave them as is::

    >>> from telwoord import cardinal

    >>> numbers = (0, 1, 2, 3, 19, 20, 30, 31, 100, 200, 215, 300, 14999, 15000, 1000000, 12345678)

    >>> for n in numbers: print("{0: 10d}   {1}".format(n, cardinal(n)))
             0   nul
             1   een
             2   twee
             3   drie
            19   negentien
            20   twintig
            30   dertig
            31   31
           100   honderd
           200   tweehonderd
           215   215
           300   driehonderd
         14999   14999
         15000   15 duizend
       1000000   1 miljoen
      12345678   12345678

To forcibly spell out all the numbers, pass ``friendly=False``::

    >>> for n in numbers: print("{0: 10d}   {1}".format(n, cardinal(n, friendly=False)))
             0   nul
             1   een
             2   twee
             3   drie
            19   negentien
            20   twintig
            30   dertig
            31   eenendertig
           100   honderd
           200   tweehonderd
           215   tweehonderdvijftien
           300   driehonderd
         14999   veertienduizend negenhonderdnegenennegentig
         15000   vijftienduizend
       1000000   een miljoen
      12345678   twaalf miljoen driehonderdvijfenveertigduizend zeshonderdachtenzeventig

In addition to cardinal numbers, you can also convert a number into its ordinal
string representation using ``telwoord.ordinal()``::

    >>> from telwoord import ordinal

    >>> for n in numbers: print("{0: 10d}   {1}".format(n, ordinal(n)))
             0   nulde
             1   eerste
             2   tweede
             3   derde
            19   negentiende
            20   twintigste
            30   dertigste
            31   31e
           100   honderdste
           200   tweehonderdste
           215   215e
           300   driehonderdste
         14999   14999e
         15000   15 duizendste
       1000000   1 miljoenste
      12345678   12345678e

The ``telwoord.ordinal()`` function also takes a ``friendly`` argument that
works the same way as for ``telwoord.cardinal()``.


Spelling rules and style recommendations
========================================

* Taalunie, `Aaneenschrijven van telwoorden
  <http://woordenlijst.org/leidraad/6/9/>`_

* Genootschap Onze Taal, `Getallen in letters of cijfers
  <https://onzetaal.nl/taaladvies/advies/getallen-in-letters-of-cijfers>`_

* Genootschap Onze Taal, `Getallen uitschrijven
  <https://onzetaal.nl/taaladvies/advies/getallen-uitschrijven>`_


Version history
===============

* 0.4

  * Improved friendly representation for some negative numbers

* 0.3

  * Implemented support for ordinal numbers

* 0.2

  * Improved support for friendly representation of negative numbers

* 0.1

  * Initial release
  * Support for spelling out numbers, optionally in a friendly way


Development
===========

To install from a source tree::

    $ pip install -e .

To run the tests you will need a few extra packages::

    $ pip install -r test-requirements.txt

To run the tests::

    $ py.test

To test against multiple Python versions::

    $ tox

Possible future work:

* Fractions, e.g. "tweederde", "twaalf tachtigste"
