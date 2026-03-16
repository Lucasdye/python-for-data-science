# -------------------- modules ----------------
from __future__ import annotations
from typing import Any


# -------------------- classes ----------------
class Array2DErrors(Exception):
    """
    Excapection base class for Array2D program
    """


class ValidationError(Array2DErrors):
    """
    Concerns all input validation errors
    """


# -------------------- helpers ----------------
def _plumb_array(array: Any) -> int:
    """Returns the max depth plumbed in the array."""
    idx = 0
    res = []

    if not isinstance(array, list):  # Base Case
        return 0
    else:
        length = len(array)
        if not length:
            return 1  # is list = depth, but empty
        while idx < length:
            res.append(1 + _plumb_array(array[idx]))  # Recursive case
            idx = idx + 1
    return max(res)


def _is_2D(array: list[Any]) -> bool:
    """Checks if the array is a 2 dimensional array."""
    dim = _plumb_array(array)
    if dim != 2:
        return False
    return True


def _is_rectangular(array: list[list]) -> bool:
    """Evaluates if the array is rectangular."""
    res = [len(el) for el in array]
    if min(res) == max(res):
        return True
    return False


def _is_number(x: Any) -> bool:
    """Checks if x is a number (int)."""
    return isinstance(x, int) and not isinstance(x, bool)


def _is_positive(x: int) -> bool:
    """Checks if the number 'x' is positive."""
    if x >= 0:
        return True
    return False


def _validate_slice_me_inputs(family: list[Any],
                              start: int, end: int) -> None:
    """
    Validates the inputs going to be send
    to slice_me().

    Args:
        family (list[Any]): array
        start (int): slice array from 'start'
        end (int): slice array to 'end'
    """
    if not isinstance(family, list):
        raise ValidationError("'family' must be a list")
    if not _is_2D(family):
        raise ValidationError("'family' must be a 2D array.")
    if any(not isinstance(el, list) for el in family):
        raise ValidationError("'family' elements must only be list")
    if not _is_rectangular(family):
        raise ValidationError("'family' must be rectangular.")
    if not _is_number(start):
        raise ValidationError("'start' must be int.")
    if not _is_number(end):
        raise ValidationError("'end' must be int.")
    if not start < len(family):
        raise ValidationError("'start' is out of bound.")
    if not end <= len(family):
        raise ValidationError("'end' is out of bound.")
    if not _is_positive(start):
        start = start + len(family)
        if not _is_positive(start):
            raise ValidationError("'start' is out of bound.")
    if not _is_positive(end):
        end = end + len(family)
        if not _is_positive(end):
            raise ValidationError("'end' is out of bound.")
    if not start < end:
        raise ValidationError("'start' must begin before 'end'.")


def _print(family: list, sliced_family: list):
    """prints shapes of family and sliced_family"""
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(sliced_family)}, {len(sliced_family[0])})")
    print(sliced_family)


# --------------------- method -----------------
def slice_me(family: list[Any], start: int, end: int) -> list[list] | None:
    """Securely slices 'family' from 'start' to 'end'
    and prints its shape.

    Args:
        family (list[Any]): 2D list to be sliced
        start (int): slicing start
        end (int): slicing end

    Returns:
        list[list]: sliced copy of family
    """
    try:
        _validate_slice_me_inputs(family, start, end)
        sliced_family = family[start:end]
        _print(family, sliced_family)
    except ValidationError as e:
        print(f"Error: {e}")
        return None
    return sliced_family


# -------------------- main --------------------
def main():
    """
    This program securely slices 2D arrays.
    """
    return


if __name__ == "__main__":
    main()
