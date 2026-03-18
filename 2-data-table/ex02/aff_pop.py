# -------------------- Modules --------------------
import pandas as pd
from pandas import DataFrame
from tabulate import tabulate as tb
from matplotlib import pyplot as plt
import os
from dataclasses import dataclass
from load_csv import load
import logging
from logging import Logger
from typing import Any
import numpy as np
import random


# -------------------- Classes --------------------
@dataclass(frozen=True)
class Params():
    project_dir: str = os.path.expanduser("~/coding/42/python-for-data-science/2-data-table")
    exercise_dir: str = os.path.dirname(__file__)
    prg_name: str = os.path.splitext(os.path.basename(__file__))[0]

    @property
    def inputs_dir(self):
        return os.path.join(self.project_dir, "inputs")

    @property
    def data_path(self):
        return os.path.join(self.inputs_dir, "population_total.csv")

    @property
    def log_name(self):
        return f"{self.prg_name}.log"

    @property
    def log_dir(self):
        return os.path.join(self.exercise_dir, "logs")

    @property
    def log_path(self):
        return os.path.join(self.exercise_dir, self.log_dir, self.log_name)


class AFFLifeError(Exception):
    """Custom base class"""

class ValidationError(AFFLifeError):
    """Raises any invalid inputs errors"""

# -------------------- Helpers --------------------
def _setup_logging() -> None:
    """Creates 'log' dir and configures the logging behavior"""
    params = Params()
    os.makedirs(params.log_dir, exist_ok=True)
    fmt = (
            '%(asctime)s %(levelname)s: %(message)s\n'
            '%(filename)s, %(funcName)s, line %(lineno)s'
        )
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        datefmt="%H:%M:%S",
        handlers=[
            # logging.StreamHandler(),
            logging.FileHandler(params.log_path, mode="w")
        ]
    )
    return


def _get_logger(name: str = None) -> Logger:
    """Returns root or named logger"""
    if not name:
        return logging.getLogger()
    else:
        return logging.getLogger(name)


def _validate_aff_life_inputs(df: Any, my_country: Any) -> None:
    if "country" not in df.columns:
        raise ValidationError("There's no 'country' column label in DataFrame")
    if my_country not in df["country"].values:
        raise ValidationError(f"{my_country} hasn't been found in DataFrame")

def _parse_population(val: Any) -> float | int:
    val = str(val)
    if "M" in val:
        return float(val.replace("M", ""))
    elif "k" in val:
        return float(val.replace("k", "")) / 100
    else:
        return float(val)

def _plot_country_pop(df: DataFrame, country: str) -> None:
    # ----- x axis -----
    row = df[df["country"] == country]
    x_years = row.columns[1:250].values.astype(int)

    # ----- y axis -----
    raw_values = row.values.flatten()[1:250]
    y_pop = [_parse_population(val) for val in raw_values]
    y_pop = np.array(y_pop, dtype="float")
    
    # ---- plot ------
    plt.plot(x_years, y_pop, label=country)

# -------------------- Methods --------------------
def aff_pop(df: DataFrame, my_country: str) -> None:
    _validate_aff_life_inputs(df, my_country)
    _plot_country_pop(df, "France")
    rdm_country = df["country"].values.flatten()[random.randrange(0, 196, 1)]
    _plot_country_pop(df, rdm_country)
  
    # ---- plot ------
    plt.legend()
    plt.show()


# -------------------- Main -----------------------
def main():
    """Displays the country's life expectancy of the 42 campus"""
    try:
        try:
            params = Params()
            _setup_logging()
            logger = _get_logger()
            logger.info("Program %s has started", params.prg_name)

            df = load(params.data_path)
            if df is None:
                raise ValidationError(f"{params.data_path} couldn't be loaded")

            aff_pop(df, "France")
        except ValidationError as e:
            logger.error(e)
            print("Error:", e)
            exit(1)
    except Exception as e:
        logger.exception("Unexpected error")
        print(f"Unexpected error: {e}")
        exit(1)
    logger.info("Program %s has finished successfully !", params.prg_name)

if __name__ == "__main__":
    main()