# coding: UTF-8

from __future__ import unicode_literals

import re

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

MILLION = 10 ** 6
BILLION = 10 ** 9
TRILLION = 10 ** 12
QUADRILLION = 10 ** 15

# Regex for numbers that should get a "-de" suffix in their ordinal form
RE_ORDINAL_SUFFIX_DE = re.compile(
    '(?:nul|twee|vier|vijf|zes|zeven|negen|tien|elf|twaalf)$')


def cardinal(n, friendly=True):
    """Convert a number into its Dutch written form for cardinal numerals.

    This function converts 1 into "een", 2 into "twee", and so on.

    If `friendly` is `True` (the default), this function uses various
    heuristics for "human friendly" results.

    If `friendly` is `False`, the number is always spelled out in full,
    which will result in not so readable results for many larger
    numbers.
    """
    if friendly:
        n_abs = abs(n)

        if n_abs < 20:
            return cardinal(n, friendly=False)

        if n_abs < 100 and n_abs % 10 == 0:
            return cardinal(n, friendly=False)

        if n_abs < 1000 and n_abs % 100 == 0:
            return cardinal(n, friendly=False)

        if n_abs < 12000 and n_abs % 1000 == 0:
            return cardinal(n, friendly=False)

        prefix = "min " if n < 0 else ""

        if n_abs < MILLION:
            q, r = divmod(n_abs, 1000)
            if r == 0:
                return prefix + "%d duizend" % q

        if n_abs < BILLION:
            q, r = divmod(n_abs, MILLION)
            if r == 0:
                return prefix + "%d miljoen" % q

        # No friendly variant, just return the numerical representation.
        return unicode(n)

    # Code below completely spells out each number.

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
        a = cardinal(q, friendly=False) if q > 1 else ""
        b = cardinal(r, friendly=False) if r > 0 else ""
        return a + "honderd" + b

    if 1000 < n < 10000 and n % 1000:
        # Special case for numbers that are exactly divisble by 100, but
        # not by 1000, e.g. "tweeëntwintighonderd"
        q, r = divmod(n, 100)
        if r == 0:
            a = cardinal(q, friendly=False) if q > 1 else ""
            return a + "honderd"

    if n < MILLION:
        q, r = divmod(n, 1000)
        a = cardinal(q, friendly=False) if q > 1 else ""
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + "duizend" + b

    if n < BILLION:
        q, r = divmod(n, MILLION)
        a = cardinal(q, friendly=False)
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + " miljoen" + b

    if n < TRILLION:
        q, r = divmod(n, BILLION)
        a = cardinal(q, friendly=False)
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + " miljard" + b

    if n < QUADRILLION:
        q, r = divmod(n, TRILLION)
        a = cardinal(q, friendly=False)
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + " biljoen" + b

    # Fallback to numerical representation
    return unicode(n)


def ordinal(n, friendly=True):
    """Convert a number into its Dutch written form for ordinal numerals.

    This function converts 1 into "eerste", 2 into "tweede", and so on.

    See the ``cardinal()`` function for a description of the
    ``friendly`` argument.
    """

    c = cardinal(n, friendly=friendly)

    if c == unicode(n):
        # No words at all. Add -e suffix, e.g. "123e"
        return c + 'e'

    # Special case for "eerste"
    if c.endswith('een'):
        return c[:-1] + 'rste'

    # Special case for "derde"
    if c.endswith('drie'):
        return c[:-3] + 'erde'

    # Several numbers: "-de"
    if RE_ORDINAL_SUFFIX_DE.search(c):
        return c + "de"

    # Everything else: "-ste"
    return c + 'ste'
