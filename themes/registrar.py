import logging


logger = logging.getLogger(__name__)


def register(include=None, exclude=None, enable=None):
    if include is None:
        include = ["matplotlib", "altair"]
    if exclude is not None:
        include = [v for v in include if v not in exclude]
    logger.info(f"Trying to registering themes to {include}")

    if "matplotlib" in include:
        try:
            import matplotlib as mpl
            import matplotlib.pyplot as plt

            logger.info("Registering themes to matplotlib")

            for name, theme in custom_themes.items():
                logger.info(f"Registering '{name}' theme to matplotlib")
                plt.style.library.update({name: mpl.RcParams(theme["matplotlib"])})
                plt.style.available[:] = sorted(plt.style.library.keys())

            if enable is not None:
                logger.info(f"Enabling {enable} for matplotlib")
        except ImportError:
            pass

    if "altair" in include:
        try:
            import altair as alt

            logger.info("Registering themes to altair")
            for name, theme in custom_themes.items():
                logger.info(f"Registering '{name}' theme to altair")
                alt.themes.register(name, theme["altair"])

            if enable is not None:
                logger.info(f"Enabling {enable} for altair")

        except ImportError:
            pass


custom_themes = {
    "capon": {
        "altair": lambda: {
            "config": {
                "background": "#fff1e5",
            }
        },
        "matplotlib": {"figure.facecolor": "#fff1e5", "axes.facecolor": "#fff1e5"},
    }
}
