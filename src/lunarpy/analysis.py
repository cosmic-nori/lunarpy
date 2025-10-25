"""
analysis.py
Provides analysis functions for lunar data.
"""

import pandas as pd
import matplotlib.pyplot as plt


def compute_summary_statistics(df):
    """
    Compute summary statistics of the dataset.
    Returns a DataFrame with descriptive statistics.
    """
    return df.describe()


def plot_variable_distribution(df, variable='crater_diameter'):
    """
    Plot the distribution of a specified variable from the lunar data.
    """
    plt.figure()
    df[variable].hist()
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {variable}')
    plt.tight_layout()
    return plt
