from themes.themes.capon_theme import capon_theme

expected_themers = []

try:
    import matplotlib
    from themes.themers.matplotlib import MatplotlibThemer

    expected_themers.append(MatplotlibThemer)
except ImportError as err:
    pass


try:
    import altair
    from themes.themers.altair import AltairThemer

    expected_themers.append(AltairThemer)
except ImportError as err:
    pass


def test_themers():
    print(f"Testing {expected_themers}")
    for themer in expected_themers:
        print(f"\n============ {themer}")
        print(themer.list())
        # themer.transform(capon_theme)()
        themer.register("capon", capon_theme)
        print(themer.list())
