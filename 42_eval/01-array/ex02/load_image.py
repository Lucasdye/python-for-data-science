# --------------------Modules--------------------
import cv2 as cv
import numpy as np
import os


# -------------------- classes --------------------
class LoadImageError(Exception):
    """Base class of the program load_image"""


class ValidationError(LoadImageError):
    """Raised when load_image input is invalid"""


# -------------------- helpers --------------------
def _validate_load_image_inputs(path: str) -> None:
    """Parses the conformity of the path.

    Raises:
        ValidationError: Raised when input is invalid
    """
    if not isinstance(path, str):
        raise ValidationError(f"'path' isn't a string '{path}'")
    if not os.path.isfile(path):
        raise ValidationError(f"File not found '{path}'")
    if cv.imread(path, cv.IMREAD_COLOR) is None:
        raise ValidationError(f"File unreadable or unsupported '{path}'")
    return


def _print(im):
    """Outputs image's shape and pixel content"""
    im_shape = im.shape
    im_content = im
    print(f"The shape of image is: {im_shape}\n{im_content}")
    return


# -------------------- methods --------------------
def ft_load(path: str) -> np.ndarray | None:
    """Loads an image (JPEG or JPG) in RGB format
    and prints infos.
    Args:
        path (str): path of the image to be loaded

    Returns:
        np.ndarray: the pixel content or None if error.
    """
    try:
        _validate_load_image_inputs(path)
        im = cv.imread(path, cv.IMREAD_COLOR)
        im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        _print(im)
    except ValidationError as e:
        print(f"Error:{e}")
        return None
    return im


def main():
    """Program that loads images"""
    return


if __name__ == "__main__":
    main()
