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
from numpy import ndarray
import random


# -------------------- Classes --------------------
@dataclass(frozen=True)
class Params():
    """Contains all the constants needed by the script"""
    project_dir: str = os.path.expanduser("~/coding/42/python-for-data-science/2-data-table")
    exercise_dir: str = os.path.dirname(__file__)
    prg_name: str = os.path.splitext(os.path.basename(__file__))[0]

    @property
    def inputs_dir(self):
        return os.path.join(self.project_dir, "inputs")

    @property
    def data_income_per_person_path(self):
        return os.path.join(self.inputs_dir, "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    @property
    def data_life_expectancy_path(self):
        return os.path.join(self.inputs_dir, "life_expectancy_years.csv")

    @property
    def data_pop_total_path(self):
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


def _validate_projection_life_inputs(df_gdp_per_capita: Any, df_life_exp: Any) -> None:
    """Validates the inputs of of aff_pop bedore being to sent to it"""
    if not (isinstance(df_gdp_per_capita, DataFrame) and isinstance(df_gdp_per_capita, DataFrame)):
        raise ValidationError(f"Datas has to be DataFrame, not '{type(df_gdp_per_capita)}' '{type(df_life_exp)}'")
    if "1900" not in df_gdp_per_capita.columns or "1900" not in df_life_exp.columns:
        raise ValidationError("There's no '1900' column label in DataFrame")


# -------------------- Methods --------------------
def projection_life(df_gdp_per_capita: DataFrame, df_life_exp: DataFrame) -> None:
    """Crosses the life expectancy data to the gdp per capita data
    of the year 1900 in the world. Offers a scatter reprensation and a
    logarithmic x axis scaling.

    Args:
        df_gdp_per_capita (DataFrame): gdp per capita per country
        df_life_exp (DataFrame): life expectancy per country
    """

    _validate_projection_life_inputs(df_gdp_per_capita, df_life_exp)
    life_exp = df_life_exp["1900"].astype(float)
    gdp_per_capita = df_gdp_per_capita["1900"].astype(float)

    plt.title("1900")
    plt.scatter(gdp_per_capita, life_exp)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()
    return


# -------------------- Main -----------------------
def main():
    """Displays the country's life expectancy of the 42 campus
    and another random country life expectancy"""
    try:
        try:
            params = Params()
            _setup_logging()
            logger = _get_logger()
            logger.info("Program %s has started", params.prg_name)

            df_gdp_per_capita = load(params.data_income_per_person_path)
            df_life_exp = load(params.data_life_expectancy_path)
            if df_gdp_per_capita is None or df_life_exp is None:
                raise ValidationError(f"{params.data_income_per_person_path} or {params.df_life_exp} couldn't be loaded")

            projection_life(df_gdp_per_capita, df_life_exp)
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