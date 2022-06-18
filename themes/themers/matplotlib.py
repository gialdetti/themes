import logging
import matplotlib as mpl
import matplotlib.pyplot as plt

from .base import BaseThemer


logger = logging.getLogger(__name__)


class MatplotlibThemer(BaseThemer):
    def register(name, theme):
        logger.info(f"Registering '{name}' theme to matplotlib")
        plt.style.library.update(
            {name: mpl.RcParams(MatplotlibThemer.transform(theme))}
        )
        plt.style.available[:] = sorted(plt.style.library.keys())

    def enable(name):
        raise NotImplementedError

    def list():
        return plt.style.available

    def transform(theme):
        return {
            "figure.facecolor": theme["paper"]["color"],
            "axes.facecolor": theme["paper"]["color"],
        }
