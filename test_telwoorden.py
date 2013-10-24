
import telwoord


def test_telwoorden():

    inputs = {
        # Normal numbers
        0: "nul",
        1: "een",
        2: "twee",
        20: "twintig",
        22: "tweeëntwintig",
        # 200: "tweehonderd",
        # 222: "tweehonderdtweeëntwintig",
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
