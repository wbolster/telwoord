Telwoord
========

A Python library to convert numerals into their Dutch written form.


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

`Aaneenschrijven van telwoorden <http://woordenlijst.org/leidraad/6/9/>`_:

* "We schrijven een getal in één woord, tot en met het woord duizend. Na het
  woord duizend volgt een spatie. De woorden miljoen, miljard, biljoen enz.
  schrijven we los."

* "Rangtelwoorden in woorden worden op dezelfde manier geschreven."

* "Een rangtelwoord dat we met een cijfer schrijven, gevolgd door e of door
  ste/de, krijgt geen apostrof."

* "De teller en de noemer van een breuk schrijven we los, behalve als die deel
  uitmaakt van een meerledige samenstelling."


Possible future work
====================

* Ordinal numbers

* Fractions


Development
===========

To run the tests::

    $ py.test
