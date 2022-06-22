import logging
import matplotlib as mpl
import matplotlib.pyplot as plt

from themes.themers.base import BaseThemer


logger = logging.getLogger(__name__)


class MatplotlibThemer(BaseThemer):
    def register(name, theme):
        logger.info(f"Registering '{name}' theme to matplotlib")
        rc_params = MatplotlibThemer.transform(theme)

        incompatible_params = {
            k: v for k, v in rc_params.items() if not k in mpl.rcParams
        }
        if len(incompatible_params) > 0:
            logger.info(
                f"Remvoing {len(incompatible_params)} incompatible params (HINT: matplotlib can be upgraded): {incompatible_params}"
            )
            rc_params = {k: v for k, v in rc_params.items() if k in mpl.rcParams}

        plt.style.library.update({name: mpl.RcParams(rc_params)})
        plt.style.available[:] = sorted(plt.style.library.keys())

    def enable(name):
        plt.style.use(name)

    def list():
        return plt.style.available

    def transform(theme):
        return {
            # Figure
            "figure.facecolor": theme["paper"]["color"],
            # Axes
            "axes.facecolor": theme["paper"]["color"],
            "axes.linewidth": 0.5,
            "axes.edgecolor": theme["axis"]["grid"]["color"],
            "axes.labelcolor": theme["axis"]["title"]["color"],
            "axes.grid": True,
            "axes.prop_cycle": mpl.cycler(color=theme["coloring"]["categorical"]),
            # Grid
            "grid.color": theme["axis"]["grid"]["color"],
            "grid.linewidth": 0.5,
            # Axis
            "xtick.color": theme["axis"]["grid"]["color"],
            "xtick.labelcolor": theme["axis"]["label"]["color"],
            "xtick.major.width": 0.5,
            "xtick.minor.width": 0.5,
            "ytick.color": theme["axis"]["grid"]["color"],
            "ytick.labelcolor": theme["axis"]["label"]["color"],
            "ytick.major.width": 0.5,
            "ytick.minor.width": 0.5,
        }
