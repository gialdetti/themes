from typing import TypedDict


class Paper(TypedDict):
    color: str


class BaseTheme(TypedDict):
    paper: Paper


capon_theme = BaseTheme({"paper": {"color": "#fff1e5"}})
capon_theme
