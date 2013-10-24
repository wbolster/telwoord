# coding: UTF-8

"""
Convert numerals into their Dutch written form.

"""

from __future__ import unicode_literals

try:
    unicode
except NameError:
    # Python 3
    unicode = str

UNITS = [
    "nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven",
    "acht", "negen", "tien", "elf", "twaalf", "dertien", "veertien",
    "vijftien", "zestien", "zeventien", "achttien", "negentien"]

TENS = [
    None, "tien", "twintig", "dertig", "veertig", "vijftig", "zestig",
    "zeventig", "tachtig", "negentig"]


def cardinal(n, threshold=None):

    if threshold is not None and abs(n) >= threshold:
        return unicode(n)

    if n < 0:
        return "min " + cardinal(abs(n))

    if n <= 19:
        return UNITS[n]

    if n <= 100:
        a, b = divmod(n, 10)
        t = TENS[int(n / 10)]
        if b == 0:
            return t
        u = cardinal(b)
        joiner = "en" if not u.endswith("e") else "ën"
        return u + joiner + t

    raise NotImplementedError("Don't know how to convert %d" % n)


def ordinal(n):
    raise NotImplementedError("Ordinal numbers not yet implemented")


# Aliases

hoofd = n = cardinal
rang = nth = ordinal
