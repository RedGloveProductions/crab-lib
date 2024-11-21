"""
Crab-Lib: A Custom Library for Analyzing GPS Data of Fishing Grounds

Author: [Your Name]
Description:
    Crab-Lib is a Python library designed for processing, analyzing, and visualizing
    GPS data from fishing grounds in the Gulf of Mexico.

Modules:
    - io: Functions for reading and writing data.
    - preprocessing: Functions for cleaning and filtering GPS data.
    - analysis: Functions for analyzing GPS data (e.g., clustering, distances).
    - visualization: Functions for creating plots and maps.
    - utils: Helper functions for common operations (e.g., coordinate transformations).

Usage:
    Import this library to work with GPS data efficiently:
    >>> import crab_lib
    >>> data = crab_lib.load_csv("fishing_data.csv")
"""

# Import core modules for direct access via the library
from .io import load_csv, save_csv
from .preprocessing import clean_data, filter_data
from .analysis import calculate_distances, find_clusters
from .visualization import plot_points, create_heatmap
from .utils import convert_coordinates, calculate_bearing

# Metadata
__version__ = "1.0.0"
__author__ = "Joe Stem"
__license__ = "GNU"

# Expose main functions for easier access
__all__ = [
    "load_csv",
    "save_csv",
    "clean_data",
    "filter_data",
    "calculate_distances",
    "find_clusters",
    "plot_points",
    "create_heatmap",
    "convert_coordinates",
    "calculate_bearing",
]
