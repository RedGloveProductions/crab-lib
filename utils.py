"""
Utils Module for Crab-Lib

This module provides utility functions for common tasks such as coordinate transformations,
bearing calculations, and other reusable operations.

Functions:
    - convert_coordinates: Converts between coordinate formats (e.g., DMS to decimal degrees).
    - calculate_bearing: Calculates the initial bearing between two GPS points.
    - is_within_bounds: Checks if a point is within a given bounding box.
"""

from typing import Tuple


def convert_coordinates(dms: str) -> float:
    """
    Converts coordinates from Degrees, Minutes, Seconds (DMS) format to decimal degrees.

    Args:
        dms (str): A string representing the coordinate in DMS format. Example: "25°46'26.5\"N"

    Returns:
        float: The coordinate in decimal degrees format.

    Raises:
        ValueError: If the input format is invalid.
    """
    try:
        dms = dms.strip()
        direction = dms[-1]
        degrees, minutes, seconds = map(float, dms[:-1].replace("°", " ").replace("'", " ").replace("\"", "").split())

        decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
        if direction in ['S', 'W']:
            decimal_degrees = -decimal_degrees

        return decimal_degrees
    except Exception as e:
        raise ValueError(f"Invalid DMS format: {dms}") from e


def calculate_bearing(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Calculates the initial bearing (forward azimuth) between two GPS points.

    Args:
        coord1 (Tuple[float, float]): The starting point (latitude, longitude).
        coord2 (Tuple[float, float]): The destination point (latitude, longitude).

    Returns:
        float: The initial bearing in degrees from the starting point to the destination.
    """
    from math import radians, degrees, atan2, cos, sin

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlon = lon2 - lon1
    x = sin(dlon) * cos(lat2)
    y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)

    initial_bearing = atan2(x, y)
    initial_bearing = degrees(initial_bearing)
    return (initial_bearing + 360) % 360


def is_within_bounds(coord: Tuple[float, float], bounds: Tuple[float, float, float, float]) -> bool:
    """
    Checks if a coordinate is within a specified bounding box.

    Args:
        coord (Tuple[float, float]): The coordinate to check (latitude, longitude).
        bounds (Tuple[float, float, float, float]): The bounding box defined as
                                                    (min_lat, max_lat, min_lon, max_lon).

    Returns:
        bool: True if the coordinate is within the bounding box, False otherwise.
    """
    lat, lon = coord
    min_lat, max_lat, min_lon, max_lon = bounds

    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon
