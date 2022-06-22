import yaml

paper_color = "#fff1e5"
paper_color_dark = "#f2dfce"

light_color = "#D5CDBE"
med_color = "#606060"
dark_color = "#3C3C3C"


textColor = dark_color
# gridColor = "#DEDDDD"
gridColor = light_color
axisColor = gridColor

# axisColor = "red"
# gridColor = "green"

status = {
    "primary": None,
    "secondary": None,
    "danger": "#c00",
    "success": "#458b00",
    "warning": None,
    "info": None,
    "light": None,
    "dark": None,
}

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


capon_theme_spec = f"""
paper:
    color: "{paper_color}"

font:
    family: "Palatino"
    color: "{textColor}"

title:
    font:
        size: 18
    anchor: "start"

axis:
    title: 
        color: "{textColor}"
    label:
        color: "{med_color}"
    domain:
        color: "{axisColor}"
    grid: 
        color: "{gridColor}"

coloring:
    categorical: {schemes["qualitative"]["Set1"]}
"""


capon_theme = yaml.safe_load(capon_theme_spec)
capon_theme


if False:
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.palplot([c for c in status.values() if c is not None])

    for t, tschemes in schemes.items():
        print(t)
        for name, colors in tschemes.items():

            sns.palplot(colors)
            plt.title(f"{t}.{name}")
