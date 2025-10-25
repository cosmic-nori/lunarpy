# lunarpy

`lunarpy` is a Python package for analyzing lunar data. It provides utilities for loading sample lunar surface data, computing summary statistics, and plotting distributions to explore key characteristics of lunar datasets. The package is designed as an educational starting point for developing more advanced lunar analysis workflows.

## Features

- Load sample lunar surface measurements such as crater diameter, depth, and albedo.
- Compute summary statistics for data frames using pandas.
- Plot variable distributions with matplotlib for exploratory analysis.
- Includes a Jupyter notebook example demonstrating usage.

## Installation

You can install `lunarpy` from source. Clone this repository and install it with pip:

```bash
git clone https://github.com/cosmic-nori/lunarpy.git
cd lunarpy
pip install .
```

This project uses a `pyproject.toml` file for packaging. Dependencies such as pandas, numpy, and matplotlib will be installed automatically.

## Usage

After installation, you can import the package and use its functions. Below is a short example demonstrating how to load the sample data, compute summary statistics, and plot a distribution:

```python
from lunarpy.data import load_sample_lunar_surface_data
from lunarpy.analysis import compute_summary_statistics, plot_variable_distribution

# Load sample dataset
df = load_sample_lunar_surface_data()

# Display summary statistics
summary = compute_summary_statistics(df)
print(summary)

# Plot the distribution of crater diameter
plot_variable_distribution(df, variable="crater_diameter")
```

For a hands-on demonstration, open the example notebook located in `notebooks/example_notebook.ipynb`. The notebook walks through loading the sample data, computing statistics, and generating a histogram.

## Project Structure

```
lunarpy/
├── pyproject.toml    # Packaging configuration
├── README.md         # Project overview and instructions
├── src/
│   └── lunarpy/
│       ├── __init__.py    # Package initializer
│       ├── data.py        # Functions for loading sample datasets
│       └── analysis.py    # Functions for summary statistics and plotting
└── notebooks/
    └── example_notebook.ipynb    # Sample Jupyter notebook
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or additional functionality.
