# themes
> _themes: style once, plot everywhere_

Universal theme styling across the different python visualization libraries. The package also contains out-of-the-box themes (e.g., a financial news theme) for instant use.

## Quickstart

```python
import themes
from themes import datasets

themes.register()
markets = datasets.load_markets()

with plt.style.context('capon'):
    markets.pivot_table(index='timestamp', columns='symbol', values='relative_price').plot()
```

The full example in a live notebook is provided [below](#examples).

## Installing
### Install latest release version via [pip](https://pip.pypa.io/en/stable/quickstart/)
```bash
$ pip install themes
```

### Install latest development version via [pip](https://pip.pypa.io/en/stable/quickstart/)
```bash
pip install git+https://github.com/gialdetti/themes.git
```

### Install latest development version in development mode
```bash
git clone git@github.com:gialdetti/themes.git
cd themes
pip install -e .
```

## Help and Support

### Examples
All examples are located in [examples](examples) folder.

|     Theme    |   MyBinder   | Colab |
| ------------ | :----------: | :---: |
| [Markets](https://nbviewer.jupyter.org/github/gialdetti/themes/blob/main/examples/plot-markets.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gialdetti/themes/main?filepath=examples/plot-markets.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gialdetti/themes/blob/main/examples/plot-markets.ipynb) | 

### Testing
After installation, you can launch the test suite:
```bash
$ pytest
```
