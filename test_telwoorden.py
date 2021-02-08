# coding: UTF-8

from __future__ import unicode_literals

import pytest

from telwoord import cardinal, ordinal


def custom_sorted(d):
    """Order by increasing values, with negative numbers coming last"""
    return sorted(d.items(), key=lambda x: (x[0] <= 0, abs(x[0])))


@pytest.mark.parametrize(
    ('number', 'expected'),
    custom_sorted({
        # Normal numbers
        0: "nul",
        1: "een",
        11: "elf",
        19: "negentien",
        20: "twintig",
        21: "eenentwintig",
        23: "drieëntwintig",
        100: "honderd",
        200: "tweehonderd",
        999: "negenhonderdnegenennegentig",
        1000: "duizend",
        2000: "tweeduizend",
        6000: "zesduizend",
        12001: "twaalfduizend een",
        99900: "negenennegentigduizend negenhonderd",
        99999: "negenennegentigduizend negenhonderdnegenennegentig",
        220000: "tweehonderdtwintigduizend",
        1000000: "een miljoen",
        1000012: "een miljoen twaalf",
        2000000: "twee miljoen",
        300000000: "driehonderd miljoen",
        300012013: "driehonderd miljoen twaalfduizend dertien",
        1000000000: "een miljard",
        12345678901: "twaalf miljard driehonderdvijfenveertig miljoen "
                     "zeshonderdachtenzeventigduizend negenhonderdeen",
        1000000000000: "een biljoen",
        13000000500003: "dertien biljoen vijfhonderdduizend drie",


        # From http://woordenlijst.org/leidraad/6/9/
        2: "twee",
        20: "twintig",
        22: "tweeëntwintig",
        200: "tweehonderd",
        222: "tweehonderdtweeëntwintig",
        2200: "tweeëntwintighonderd",
        2220: "tweeduizend tweehonderdtwintig",
        2220222: "twee miljoen tweehonderdtwintigduizend "
                 "tweehonderdtweeëntwintig",

        # From https://onzetaal.nl/taaladvies/advies/getallen-uitschrijven
        108: "honderdacht",
        678: "zeshonderdachtenzeventig",
        2013: "tweeduizend dertien",
        2577: "tweeduizend vijfhonderdzevenenzeventig",
        17053980: "zeventien miljoen drieënvijftigduizend negenhonderdtachtig",

        # Negative numbers
        -1: "min een",
        -10: "min tien",
        -2000: "min tweeduizend",
        -100000: "min 100 duizend",
        -20000000: "min 20 miljoen",
    }))
def test_cardinal(number, expected):
    actual = cardinal(number, friendly=False)
    assert actual == expected


@pytest.mark.parametrize(
    ('number', 'expected'),
    custom_sorted({
        0: "nul",
        1: "een",
        19: "negentien",
        20: "twintig",
        50: "vijftig",
        100: "honderd",
        101: "101",
        300: "driehonderd",
        301: "301",
        900: "negenhonderd",
        6000: "zesduizend",
        10000: "tienduizend",
        10010: "10010",
        11000: "elfduizend",
        11011: "11011",
        12000: "12 duizend",
        12001: "12001",
        13000: "13 duizend",
        100000: "100 duizend",
        10000000: "10 miljoen",

        # Negative numbers
        -12: "min twaalf",
        -312: "-312",
        -2000: "min tweeduizend",
        -100000: "min 100 duizend",
        -20000000: "min 20 miljoen",
        -20000001: "-20000001",
    }))
def test_friendly_cardinals(number, expected):
    actual = cardinal(number)
    assert actual == expected


@pytest.mark.parametrize(
    ('number', 'expected'),
    custom_sorted({
        0: "nulde",
        1: "eerste",
        2: "tweede",
        3: "derde",
        4: "vierde",
        5: "vijfde",
        6: "zesde",
        7: "zevende",
        8: "achtste",
        9: "negende",
        10: "tiende",
        11: "elfde",
        12: "twaalfde",
        13: "dertiende",
        14: "veertiende",
        15: "vijftiende",
        16: "zestiende",
        17: "zeventiende",
        18: "achttiende",
        19: "negentiende",
        20: "twintigste",
        21: "eenentwintigste",
        30: "dertigste",
        50: "vijftigste",
        100: "honderdste",
        101: "honderdeerste",
        300: "driehonderdste",
        1000: "duizendste",
        1001: "duizend eerste",
        1012: "duizend twaalfde",
        1000000: "een miljoenste",
        2000000: "twee miljoenste",
        1000000000: "een miljardste",

        # Negative numbers
        -1: "min eerste",
        -12: "min twaalfde",
    }))
def test_ordinals(number, expected):
    actual = ordinal(number, friendly=False)
    assert actual == expected


@pytest.mark.parametrize(
    ('number', 'expected'),
    custom_sorted({
        0: "nulde",
        1: "eerste",
        100: "honderdste",
        4000: "vierduizendste",
        301: "301e",
        1000: "duizendste",
        43000: "43 duizendste",
        10000000: "10 miljoenste",

        # Negative numbers
        -12: "min twaalfde",
        -312: "-312e",
    }))
def test_friendly_ordinals(number, expected):
    actual = ordinal(number)
    assert actual == expected
