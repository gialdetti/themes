from themes.themes.base import BaseTheme


textColor = "#3C3C3C"
axisColor = textColor
# gridColor = "#DEDDDD"
gridColor = "#D5CDBE"

# axisColor = "red"
# gridColor = "green"

schemes = {
    "qualitative": {
        "Set1": ["#C66254", "#EFA558", "#809E9A", "#94826A"],
        "Set2": [
            "#27757B",
            "#EEA45F",
            "#94826B",
            "#EED485",
            "#A6A371",
            "#819E9A",
            "#746E7F",
        ],
    },
    "diverging": {
        "RdGn": [
            "#9C3151",
            "#AF5771",
            "#C17E92",
            "#D4A4B3",
            "#E6CBD3",
            "#D1E1C1",
            "#AECB92",
            "#8CB564",
            "#6B9E46",
            "#478A16",
        ]
    },
    "continuous": {
        "blacks": ["#312F36", "#524F5A", "#736E7E", "#96929E", "#A8A4AE"],
        "oranges": ["#c37122", "#dd9148", "#eda45e"],
        "reds": ["#6f3029", "#933e33", "#c36256", "#d47e74", "#dba19c"],
        "blues": ["#1D2931", "#3B5361", "#587C92", "#75A5C2", "#ACC9DA"],
    },
}

capon_theme = BaseTheme(
    {
        "paper": {"color": "#fff1e5"},
        "font": {"family": "Lato", "color": textColor},
        "title": {"font": {"size": 18}, "anchor": "start"},
        "axis": {
            "title": {"color": axisColor},
            "label": {"color": "#606060"},
            "domain": {"color": axisColor},
            "grid": {"color": gridColor},
        },
        "coloring": {"categorical": schemes["qualitative"]["Set1"]},
    }
)
capon_theme
