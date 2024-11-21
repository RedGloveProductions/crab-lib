"""
I/O Module for Crab-Lib

Handles input and output operations, including reading GPS data from CSV files
and saving processed data to various formats.

Functions:
    - load_csv: Load GPS data from a CSV file.
    - save_csv: Save processed data to a CSV file.
"""

import csv
from typing import List, Dict


def load_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Loads GPS data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary
                              represents a row of the CSV file.
                              Example: [{'x': '25.774', 'y': '-80.19', 'comment': 'hotspot'}]

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not properly formatted.
    """
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            required_columns = {'x', 'y', 'comment'}

            # Validate columns
            if not required_columns.issubset(set(reader.fieldnames)):
                raise ValueError(f"CSV file must contain the columns: {required_columns}")

            # Read data
            for row in reader:
                data.append({'x': row['x'], 'y': row['y'], 'comment': row['comment']})
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {file_path}") from e

    return data


def save_csv(file_path: str, data: List[Dict[str, str]]) -> None:
    """
    Saves GPS data to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (List[Dict[str, str]]): A list of dictionaries representing the data to save.
                                     Each dictionary should have keys: 'x', 'y', and 'comment'.

    Returns:
        None

    Raises:
        ValueError: If the data format is incorrect.
    """
    if not all(isinstance(row, dict) and {'x', 'y', 'comment'}.issubset(row.keys()) for row in data):
        raise ValueError("Data must be a list of dictionaries with 'x', 'y', and 'comment' keys.")

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['x', 'y', 'comment'])
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        raise IOError(f"An error occurred while writing to the file: {file_path}") from e
