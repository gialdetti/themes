import logging
import themes


logger = logging.getLogger("themes")
logging.basicConfig()
logger.setLevel(logging.INFO)


def test_register():
    themes.register()


def test_register_mpl():
    try:
        import matplotlib.pyplot as plt

        print(plt.style.available)
        themes.register(include=["matplotlib"])
        print(plt.style.available)

    except ImportError:
        pass


def test_register_altair():
    try:
        import altair as alt

        print(alt.themes.names())
        themes.register(include=["altair"])
        print(alt.themes.names())

    except ImportError:
        pass
