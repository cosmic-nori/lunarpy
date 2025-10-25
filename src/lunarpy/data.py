"""
Data loading utilities for lunarpy.
"""

import pandas as pd
from io import StringIO

def load_sample_lunar_surface_data():
    """
    Load a sample lunar surface dataset as a pandas DataFrame.

    Returns
    -------
    pandas.DataFrame
        A sample dataset containing crater IDs, diameters, latitudes, and longitudes.
    """
    csv = """crater_id,crater_diameter,latitude,longitude
1,10.3,12.5,45.2
2,7.6,-3.2,100.1
3,15.1,25.4,-30.7
4,5.2,-42.1,76.3
"""
    return pd.read_csv(StringIO(csv))
