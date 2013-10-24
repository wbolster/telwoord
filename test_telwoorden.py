# coding: UTF-8

from __future__ import unicode_literals

import telwoord


def test_cardinal():

    inputs = {
        # Normal numbers
        0: "nul",
        1: "een",
        2: "twee",
        20: "twintig",
        22: "tweeëntwintig",
        100: "honderd",
        200: "tweehonderd",
        222: "tweehonderdtweeëntwintig",
        999: "negenhonderdnegenennegentig",
        # 1000: "duizend",
        # 2200: "tweeëntwintighonderd",
        # 2220: "tweeduizend tweehonderdtwintig",
        # 2220222: "twee miljoen tweehonderdtwintigduizend "
        #          "tweehonderdtweeëntwintig",

        # Negative numbers
        -1: "min een",
        -10: "min tien",
    }

    for n, w in inputs.items():
        assert telwoord.cardinal(n) == w


def test_threshold():
    assert telwoord.cardinal(5, threshold=7) == "vijf"
    assert telwoord.cardinal(5, threshold=3) == "5"

    assert telwoord.cardinal(-5, threshold=7) == "min vijf"
    assert telwoord.cardinal(-5, threshold=3) == "-5"
