from themes import datasets


def test_load_markets():
    markets = datasets.load_markets()
    assert markets is not None


def test_load_gapminder():
    gapminder = datasets.load_gapminder()
    assert gapminder is not None
