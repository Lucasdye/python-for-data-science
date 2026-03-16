# -------------------- modules --------------------
from __future__ import annotations
from typing import Any


# -------------------- classes ------------------
class BMIError(Exception):
    """Base class for BMI related errors"""


class ValidationError(BMIError):
    """Raised for input validation errors"""


# -------------------- helpers ------------------
def _is_number(x: Any) -> bool:
    """Evaluates if 'x' is a number (int or float)"""
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _is_positive(x: int | float) -> bool:
    """Evaluates if 'x' is strictly positive."""
    return x > 0


def _is_int(x: Any) -> bool:
    """Evaluates if 'x' is int"""
    return isinstance(x, int) and not isinstance(x, bool)


def _validate_bmi_inputs(
        heights: list[int | float],
        weights: list[int | float]
        ) -> None:
    """Evaluates bmi inputs.

    Raises:
        ValidationError: If inputs are invalid.
    """
    if not isinstance(heights, list):
        raise ValidationError("'heights' must be a list.")

    if not isinstance(weights, list):
        raise ValidationError("'weights' must be a list.")

    if len(heights) != len(weights):
        raise ValidationError("'heights' and 'weights' must be same length.")

    if any(not _is_number(height) for height in heights):
        raise ValidationError("'heights' elements must be int or float.")

    if any(not _is_number(weight) for weight in weights):
        raise ValidationError("'weights' elements must be int or float.")

    if any(not _is_positive(height) for height in heights):
        raise ValidationError("'heights' elements must be positive values.")

    if any(not _is_positive(weight) for weight in weights):
        raise ValidationError("'weights' elements must be positive values.")


def _validate_apply_limit_inputs(bmi: list[int | float], limit: int) -> None:
    """Validates apply_limit inputs.

    Raises:
        ValidationError: if inputs are invalid.
    """
    if not isinstance(bmi, list):
        raise ValidationError("'bmi' must be a list.")

    if any(not _is_number(el) for el in bmi):
        raise ValidationError("'bmi' elements must be int or float.")

    if any(el <= 0 for el in bmi):
        raise ValidationError("'bmi' numbers must be positive values.")

    if not _is_int(limit):
        raise ValidationError("'limit' must be int.")

    if not _is_positive(limit):
        raise ValidationError("'limit' must be strictly superior to 0.")


# -------------------- methods ---------------------
def apply_limit(bmi: list[int | float], limit: int) -> list[bool] | None:
    """Evaluates each bmi value against the limit.

    Args:
        bmi (list[int  |  float]): bmi values
        limit (int): limit

    Returns:
        list[bool]: returns a list of bool or None if error.
    """
    try:
        _validate_apply_limit_inputs(bmi, limit)
        res = [el > limit for el in bmi]
        print(res)
    except ValidationError as e:
        print(f"Error: {e}")
        return None
    return res


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float] | None:
    """Calculates the bmi from 'height' and 'weight'
    Args:
        height (list[int  |  float]): heights
        weight (list[int  |  float]): weights

    Returns:
        list[int | float] | None: bmi values
    """
    try:
        _validate_bmi_inputs(height, weight)
        bmi = [float(w / (h ** 2)) for h, w in zip(height, weight)]
        print(f"{bmi} {type(bmi)}", end="")
    except ValidationError as e:
        print(f"Error: {e}")
        return None
    return bmi


# -------------------- main ----------------------
def main():
    """The program is meant to calcultate the bmi
    from a list of heights and weights, and compare
    the results against a limit.
    """


if __name__ == "__main__":
    main()
