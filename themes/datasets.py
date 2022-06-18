import logging
import os
import time

import pandas as pd


def load_markets():
    """
    https://github.com/gialdetti/capon/
    """
    filename = get_resource_path("market-indexes.csv.gz")
    markets = pd.read_csv(filename, parse_dates=["timestamp"])
    return markets


def load_gapminder():
    """
    https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv
    """
    filename = get_resource_path("gapminder2007.csv")
    gapminder = pd.read_csv(filename)
    return gapminder


RESOURCES_ROOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "resources")
)
logging.info(f'RESOURCES_ROOT_PATH = "{RESOURCES_ROOT_PATH}"')


def get_resource_path(sub_path):
    return os.path.join(
        RESOURCES_ROOT_PATH, sub_path.replace("{ts}", time.strftime("(%y%m%d.%H%M%S)"))
    )
