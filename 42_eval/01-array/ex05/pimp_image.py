# -------------------- Modules --------------------
from typing import Any
import numpy as np
from numpy import ndarray
from matplotlib import pyplot as plt


# -------------------- Classes --------------------
class PimpImageError(Exception):
    """Custom base exception class for 'rotate' program"""


class ValidationError(PimpImageError):
    """Raises invalid inputs"""


# -------------------- Helpers ---------------------------
def _validate_pimp_image_inputs(im: Any) -> None:
    if not isinstance(im, ndarray):
        raise ValidationError("'im' must be an ndarray")

    if not im.ndim == 3:
        raise ValidationError("'im' must be a 3d.")

    if not (im.dtype == "uint8" or
            im.dtype == "uint32" or
            im.dtype == "uint64"):
        msg = f"Image's pixel must be type uint8/32/64, not {im.dtype}"
        raise ValidationError(msg)


def _display_image(im: np.ndarray, cmap: str = "") -> None:
    """Displays the image tensor with plt"""
    if cmap != "":
        plt.imshow(im, cmap=cmap)
    else:
        plt.imshow(im)
    plt.show()


def _print(im: np.ndarray, msg: str = "") -> None:
    """Outputs image's shape and pixel content"""
    print(msg, im.shape)


def _compute_px_luminance(px: np.array) -> np.float64:
    """computes the weighted luminance formula"""
    green_weight = 0.587
    red_weight = 0.299
    blue_weight = 0.114

    grey_px = np.ones([3], dtype="float64")
    grey_px[0] = px[0] * red_weight
    grey_px[1] = px[1] * green_weight
    grey_px[2] = px[2] * blue_weight

    grey_px = grey_px.sum()
    return grey_px


# -------------------- Public methods --------------------
def ft_grey(im: np.ndarray) -> np.ndarray | None:
    """Turns a grey shaded copy of the image"""
    try:
        len_x = im.shape[0]
        len_y = im.shape[1]

        cpy_im = im.copy()
        grey_im = np.ones([len_x, len_y, 1], dtype="uint64")
        for i in range(len_x):
            for j in range(len_y):
                grey_px = _compute_px_luminance(cpy_im[i][j])
                grey_im[i][j] = grey_px
        _print(im, "The shape of the image is: ")
        _display_image(grey_im, cmap="grey")
    except ValidationError as e:
        print("Error: ", e)
        return None
    return grey_im


def ft_invert(im: np.ndarray) -> np.ndarray | None:
    """Inverts the image's colors"""
    try:
        _validate_pimp_image_inputs(im)
        inv_im = im.copy()
        inv_im = 255 - inv_im
        _print(inv_im, "The shape of image is: ")
        _display_image(inv_im)
    except ValidationError as e:
        print("Error: ", e)
        return None
    return inv_im


def ft_red(im: np.ndarray) -> np.ndarray | None:
    """Turns the image into red shades"""
    try:
        _validate_pimp_image_inputs(im)
        red_im = im.copy()
        red_im[:, :, 1] = 0
        red_im[:, :, 2] = 0
        _print(red_im, "The shape of image is: ")
        _display_image(red_im)
    except ValidationError as e:
        print("Error: ", e)
        return None
    return red_im


def ft_blue(im: np.ndarray) -> np.ndarray | None:
    """Turns the image into blue shades"""
    try:
        _validate_pimp_image_inputs(im)
        blue_im = im.copy()
        blue_im[:, :, 0] = 0
        blue_im[:, :, 1] = 0
        _print(im, "The shape of image is: ")
        _display_image(blue_im)
    except ValidationError as e:
        print("Error: ", e)
        return None
    return blue_im


def ft_green(im: np.ndarray) -> np.ndarray | None:
    """Turns the image into green shades"""
    try:
        _validate_pimp_image_inputs(im)
        green_im = im.copy()
        green_im[:, :, 0] = 0
        green_im[:, :, 2] = 0
        _print(green_im, "The shape of image is: ")
        _display_image(green_im)
    except ValidationError as e:
        print("Error: ", e)
        return None
    return green_im


def main():
    """Transforms the colors of the image"""
    return


if __name__ == "__main__":
    main()
