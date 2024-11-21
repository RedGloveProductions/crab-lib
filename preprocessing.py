"""
Preprocessing Module for Crab-Lib

This module provides functions to clean and preprocess GPS data.
It includes functionalities for removing duplicates, handling missing
or invalid data, and filtering the dataset based on user criteria.

Functions:
    - clean_data: Removes duplicates and invalid data from the dataset.
    - filter_data: Filters the dataset based on user-defined criteria.
    - standardize_comments: Standardizes the format of comment strings.
"""

from typing import List, Dict


def clean_data(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Cleans the GPS dataset by removing duplicates and invalid rows.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries representing the dataset.
                                     Each dictionary must contain keys: 'x', 'y', 'comment'.

    Returns:
        List[Dict[str, str]]: A cleaned dataset with duplicates and invalid rows removed.

    Raises:
        ValueError: If the dataset is not in the correct format.
    """
    if not all(isinstance(row, dict) and {'x', 'y', 'comment'}.issubset(row.keys()) for row in data):
        raise ValueError("Data must be a list of dictionaries with 'x', 'y', and 'comment' keys.")

    cleaned_data = []
    seen = set()  # To track unique GPS points
    for row in data:
        try:
            # Ensure coordinates are valid floats
            x, y = float(row['x']), float(row['y'])
            key = (x, y)  # Use coordinates as the unique identifier
            if key not in seen:
                seen.add(key)
                cleaned_data.append({'x': x, 'y': y, 'comment': row['comment']})
        except ValueError:
            # Skip rows with invalid coordinates
            continue

    return cleaned_data


def filter_data(data: List[Dict[str, str]], keyword: str) -> List[Dict[str, str]]:
    """
    Filters the GPS dataset based on a keyword in the 'comment' field.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries representing the dataset.
                                     Each dictionary must contain keys: 'x', 'y', 'comment'.
        keyword (str): The keyword to filter the comments by.

    Returns:
        List[Dict[str, str]]: A filtered dataset containing only rows with comments that include the keyword.
    """
    return [row for row in data if keyword.lower() in row['comment'].lower()]


def standardize_comments(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Standardizes the format of the 'comment' field in the dataset.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries representing the dataset.

    Returns:
        List[Dict[str, str]]: The dataset with standardized comments.
                              Example: Capitalizes the first letter of each comment.
    """
    for row in data:
        row['comment'] = row['comment'].strip().capitalize()
    return data
