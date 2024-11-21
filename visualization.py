"""
Visualization Module for Crab-Lib

This module provides functions for visualizing GPS data, including plotting points,
visualizing clusters, and creating heatmaps.

Functions:
    - plot_points: Creates a scatter plot of GPS points.
    - plot_clusters: Visualizes clusters of GPS points.
    - create_heatmap: Generates a heatmap from GPS data.
"""

import matplotlib.pyplot as plt
from typing import List, Dict


def plot_points(data: List[Dict[str, float]], title: str = "GPS Points") -> None:
    """
    Plots GPS points on a 2D scatter plot.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries representing the dataset.
                                       Each dictionary must contain keys: 'x' and 'y'.
        title (str): Title of the plot. Defaults to "GPS Points".

    Returns:
        None
    """
    latitudes = [float(point['x']) for point in data]
    longitudes = [float(point['y']) for point in data]

    plt.figure(figsize=(10, 8))
    plt.scatter(longitudes, latitudes, c='blue', alpha=0.6, edgecolors='k', s=50)
    plt.title(title, fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()


def plot_clusters(clusters: List[List[Dict[str, float]]], title: str = "GPS Clusters") -> None:
    """
    Plots clusters of GPS points on a 2D scatter plot, with different colors for each cluster.

    Args:
        clusters (List[List[Dict[str, float]]]): A list of clusters, where each cluster is a list of points.
                                                 Each point must be a dictionary with 'x' and 'y' keys.
        title (str): Title of the plot. Defaults to "GPS Clusters".

    Returns:
        None
    """
    plt.figure(figsize=(10, 8))
    
    for cluster_idx, cluster in enumerate(clusters):
        latitudes = [float(point['x']) for point in cluster]
        longitudes = [float(point['y']) for point in cluster]
        plt.scatter(longitudes, latitudes, label=f"Cluster {cluster_idx + 1}", alpha=0.6, edgecolors='k', s=50)

    plt.title(title, fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.legend()
    plt.show()


def create_heatmap(data: List[Dict[str, float]], bins: int = 50, title: str = "GPS Heatmap") -> None:
    """
    Creates a 2D heatmap from GPS points.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries representing the dataset.
                                       Each dictionary must contain keys: 'x' and 'y'.
        bins (int): Number of bins for the heatmap. Defaults to 50.
        title (str): Title of the heatmap. Defaults to "GPS Heatmap".

    Returns:
        None
    """
    latitudes = [float(point['x']) for point in data]
    longitudes = [float(point['y']) for point in data]

    plt.figure(figsize=(10, 8))
    plt.hist2d(longitudes, latitudes, bins=bins, cmap='hot', density=True)
    plt.colorbar(label="Density")
    plt.title(title, fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()
