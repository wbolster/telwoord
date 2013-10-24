# coding: UTF-8

from __future__ import unicode_literals

from telwoord import cardinal


def test_cardinal():

    inputs = {
        # Normal numbers
        0: "nul",
        1: "een",
        11: "elf",
        19: "negentien",
        20: "twintig",
        23: "eenentwintig",
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
    }

    for n, w in inputs.items():
        assert cardinal(n, friendly=False) == w


def test_friendly_cardinals():
    inputs = {
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
        # -12: "min twaalf",
        # -312: "-312",
    }

    for n, w in inputs.items():
        assert cardinal(n) == w
