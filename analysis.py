"""
Analysis Module for Crab-Lib

This module provides functions for analyzing GPS data, including calculating distances,
detecting clusters, and summarizing key metrics.

Functions:
    - calculate_distances: Compute pairwise distances between all points in the dataset.
    - find_clusters: Identify clusters of points using a simple distance-based approach.
    - summarize_data: Generate a summary of the dataset, including statistics and metrics.
"""

from typing import List, Dict, Tuple
from math import radians, sin, cos, sqrt, atan2


def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Calculates the great-circle distance between two points on the Earth's surface.

    Args:
        coord1 (Tuple[float, float]): Coordinates of the first point (latitude, longitude).
        coord2 (Tuple[float, float]): Coordinates of the second point (latitude, longitude).

    Returns:
        float: Distance in kilometers between the two points.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def calculate_distances(data: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
    Computes the pairwise distances between all points in the dataset.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries representing the dataset.
                                       Each dictionary must contain keys: 'x' and 'y'.

    Returns:
        List[Dict[str, float]]: A list of dictionaries with distances between points.
                                Example: [{'point1': (25.774, -80.19), 'point2': (27.345, -82.567), 'distance': 300.2}]
    """
    distances = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            point1 = (float(data[i]['x']), float(data[i]['y']))
            point2 = (float(data[j]['x']), float(data[j]['y']))
            distance = haversine_distance(point1, point2)
            distances.append({'point1': point1, 'point2': point2, 'distance': distance})
    return distances


def find_clusters(data: List[Dict[str, float]], radius: float) -> List[List[Dict[str, float]]]:
    """
    Identifies clusters of points within a specified distance (radius).

    Args:
        data (List[Dict[str, float]]): A list of dictionaries representing the dataset.
                                       Each dictionary must contain keys: 'x' and 'y'.
        radius (float): The radius (in kilometers) to define a cluster.

    Returns:
        List[List[Dict[str, float]]]: A list of clusters, where each cluster is a list of points.
    """
    clusters = []
    visited = set()

    for i, point in enumerate(data):
        if i in visited:
            continue

        cluster = []
        visited.add(i)

        for j, other_point in enumerate(data):
            if j in visited:
                continue

            point1 = (float(point['x']), float(point['y']))
            point2 = (float(other_point['x']), float(other_point['y']))
            distance = haversine_distance(point1, point2)

            if distance <= radius:
                cluster.append(other_point)
                visited.add(j)

        clusters.append([point] + cluster)

    return clusters


def summarize_data(data: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Generates a summary of the dataset.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries representing the dataset.

    Returns:
        Dict[str, float]: A summary containing the total number of points,
                          average latitude, average longitude, and bounding box.
    """
    total_points = len(data)
    avg_lat = sum(float(point['x']) for point in data) / total_points
    avg_lon = sum(float(point['y']) for point in data) / total_points

    latitudes = [float(point['x']) for point in data]
    longitudes = [float(point['y']) for point in data]

    bounding_box = {
        "min_lat": min(latitudes),
        "max_lat": max(latitudes),
        "min_lon": min(longitudes),
        "max_lon": max(longitudes),
    }

    return {
        "total_points": total_points,
        "average_latitude": avg_lat,
        "average_longitude": avg_lon,
        "bounding_box": bounding_box,
    }
