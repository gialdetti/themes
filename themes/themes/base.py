from typing import List, Optional
from typing import TypedDict


class Paper(TypedDict):
    color: str


class Font(TypedDict):
    family: str
    color: str
    size: float


class Title(TypedDict):
    font: Font
    anchor: str


class Label:
    font: Font


class Grid(TypedDict):
    color: str


class Axis(TypedDict):
    title: Title
    label: Label
    grid: Grid


class Coloring(TypedDict):
    category: List[str]
    diverging: List[str]
    heatmap: List[str]
    ramp: List[str]


class BaseTheme(TypedDict):
    paper: Paper
    font: Font
    title: Title
    axis: Axis
    coloring: Coloring
