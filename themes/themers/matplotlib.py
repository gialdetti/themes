import logging
import matplotlib as mpl
import matplotlib.pyplot as plt

from themes.themers.base import BaseThemer


logger = logging.getLogger(__name__)


class MatplotlibThemer(BaseThemer):
    def register(name, theme):
        logger.info(f"Registering '{name}' theme to matplotlib")
        plt.style.library.update(
            {name: mpl.RcParams(MatplotlibThemer.transform(theme))}
        )
        plt.style.available[:] = sorted(plt.style.library.keys())

    def enable(name):
        plt.style.use(name)

    def list():
        return plt.style.available

    def transform(theme):
        return {
            "figure.facecolor": theme["paper"]["color"],
            "axes.facecolor": theme["paper"]["color"],
            "axes.prop_cycle": mpl.cycler(color=theme["coloring"]["categorical"]),
            "axes.grid": True,
            "grid.color": theme["axis"]["grid"]["color"],
            "grid.linewidth": ".5",
            "xtick.color": theme["axis"]["domain"]["color"],
            "ytick.color": theme["axis"]["domain"]["color"],
        }
