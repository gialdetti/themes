import logging
import altair as alt

from themes.themers.base import BaseThemer

logger = logging.getLogger(__name__)


class AltairThemer(BaseThemer):
    def register(name, theme):
        logger.info(f"Registering '{name}' theme to altair")
        alt.themes.register(name, AltairThemer.transform(theme))

    def enable(name):
        alt.themes.enable(name)

    def list():
        return alt.themes.names()

    def transform(theme):

        return lambda: {
            "config": {
                "background": theme["paper"]["color"],
                "axisX": {
                    "titleColor": theme["axis"]["title"]["color"],
                    "labelColor": theme["axis"]["label"]["color"],
                    "domainColor": theme["axis"]["domain"]["color"],
                    "gridColor": theme["axis"]["grid"]["color"],
                },
                "axisY": {
                    "titleColor": theme["axis"]["title"]["color"],
                    "labelColor": theme["axis"]["label"]["color"],
                    "domainColor": theme["axis"]["domain"]["color"],
                    "gridColor": theme["axis"]["grid"]["color"],
                },
                "range": {"category": theme["coloring"]["categorical"]},
            }
        }


if False:
    from themes.themes.capon_theme import capon_theme as theme

    display(AltairThemer.transform(theme)())

    # AltairThemer.register("capon", capon_theme)

    # import altair as alt
    # from vega_datasets import data

    # cars = data.cars()
    # alt.Chart(cars).mark_point().encode(
    #     x="Horsepower",
    #     y="Miles_per_Gallon",
    #     color="Origin",
    # ).interactive()
