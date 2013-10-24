# coding: UTF-8

"""
Convert numbers into their Dutch written form.
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

    if n < 20:
        return UNITS[n]

    if n < 100:
        q, r = divmod(n, 10)
        a = TENS[q]
        if r == 0:
            return a
        b = cardinal(r)
        joiner = "en" if not b.endswith("e") else "ën"
        return b + joiner + a

    if n < 1000:
        q, r = divmod(n, 100)
        a = cardinal(q) if q > 1 else ""
        b = cardinal(r) if r > 0 else ""
        return a + "honderd" + b

    if 1000 < n < 10000:
        # Special case for numbers that are exactly divisble by 100,
        # e.g. "tweeëntwintighonderd"
        q, r = divmod(n, 100)
        if r == 0:
            a = cardinal(q) if q > 1 else ""
            return a + "honderd"

    if n < 1000000:
        q, r = divmod(n, 1000)
        a = cardinal(q) if q > 1 else ""
        b = " " + cardinal(r) if r > 0 else ""
        return a + "duizend" + b

    # Fallback to numerical representation
    return cardinal(n, threshold=0)


def ordinal(n):
    raise NotImplementedError("Ordinal numbers not yet implemented")


# Aliases

hoofd = n = cardinal
rang = nth = ordinal
