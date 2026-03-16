# -------------------- Modules --------------------
import pandas as pd
from pandas import DataFrame
from typing import Any
import os
from tabulate import tabulate as tb

# -------------------- Classes --------------------
class LoadError(Exception):
    """Custom base class"""

class ValidationError(LoadError):
    """Raised for any input errors"""


# -------------------- Helpers --------------------
def _validate_load_inputs(path: Any) -> None:
    """Evaluates the conformity of load() inputs

    Raises:
        ValidationError: raised when input is wrong
    """
    if not os.path.exists(path):
        raise ValidationError(f"File doesn't exist '{path}'")
    dot_idx = path.rfind(".")
    extension = path[dot_idx + 1:]
    if not extension == "csv":
        raise ValidationError(f"File must be csv, not '{extension}'")


def _print(df: DataFrame) -> None:
    """Prints the df dimensions and content in a beautiful table"""
    print(f"Loading dataset of dimension {df.shape}")
    preview = df.iloc[:20, :20]
    print(tb(preview, headers="keys", tablefmt="psql"))


def load(path: str) -> DataFrame | None:
    """Loads a csv file with panda.
    Args:
        path (str): path to csv file.
    Returns:
        DataFrame | None: DataFrame or None is fail
    """
    try:
        _validate_load_inputs(path)
        df = pd.read_csv(path)
        _print(df)
    except ValidationError as e:
        print("Error: ", e)
        return None
    return df


def main():
    """Servs test purposes"""
    try:
        load("./inputs/life_expectancy_years.csv")
        load("./inputs/dummy_dataset.xlsx")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
    """This program loads a csv file """
