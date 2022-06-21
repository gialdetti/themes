import logging
from themes.themes.capon_theme import capon_theme


logger = logging.getLogger(__name__)
custom_themes = {"capon": capon_theme}


def register(include=None, exclude=None, enable=None):
    themers_map = find_themers()

    if include is None:
        include = list(themers_map.keys())
    if exclude is not None:
        include = [v for v in include if v not in exclude]
    logger.info(f"Trying to register themes to {include}")

    for themer_name in include:
        logger.info(f"Registering themes to {themer_name}")
        themer = themers_map[themer_name]
        for name, theme in custom_themes.items():
            logger.info(f"Registering '{name}' theme to {themer_name}")
            themer.register(name, theme)

    if enable is not None:
        for themer_name in include:
            logger.info(f"Enabling '{name}' in {themer_name}")
            themer = themers_map[themer_name]
            themer.enable(enable)


def find_themers():
    themers = {}

    try:
        from themes.themers.matplotlib import MatplotlibThemer

        themers["matplotlib"] = MatplotlibThemer
    except ImportError:
        pass

    try:
        from themes.themers.altair import AltairThemer

        themers["altair"] = AltairThemer
    except ImportError:
        pass

    return themers
