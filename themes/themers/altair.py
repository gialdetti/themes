import logging
import altair as alt

from .base import BaseThemer


logger = logging.getLogger(__name__)


class AltairThemer(BaseThemer):
    def register(name, theme):
        logger.info(f"Registering '{name}' theme to altair")
        alt.themes.register(name, AltairThemer.transform(theme))

    def enable(name):
        raise NotImplementedError

    def list():
        return alt.themes.names()

    def transform(theme):

        return lambda: {
            "config": {
                "background": theme["paper"]["color"],
            }
        }
