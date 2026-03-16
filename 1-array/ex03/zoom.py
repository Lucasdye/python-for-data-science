# -------------------- Modules --------------------
import os
from dataclasses import dataclass
import logging
from logging import Logger
import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray
from load_image import ft_load


# -------------------- Classes --------------------
@dataclass(frozen=True)
class Params:
    project_dir: str = os.path.expanduser(
        "~/coding/42/python-for-data-science/1-array")

    ex_dir: str = os.path.dirname(__file__)
    script_name: str = os.path.splitext(os.path.basename(__file__))[0]
    img_name: str = "animal.jpeg"

    @property
    def inputs_dir(self) -> str:
        return os.path.join(self.project_dir, "inputs")

    @property
    def img_path(self) -> str:
        return os.path.join(self.inputs_dir, self.img_name)

    @property
    def log_dir(self) -> str:
        return os.path.join(self.ex_dir, "logs")

    @property
    def log_name(self) -> str:
        return f"{self.script_name}.log"

    @property
    def log_path(self) -> str:
        return os.path.join(self.ex_dir, self.log_dir, self.log_name)


class ZoomErrors(Exception):
    """Custom base exception class for zoom program"""


class ValidationError(ZoomErrors):
    """Raises invalid inputs"""


# -------------------- Handlers --------------------
def _setup_logging() -> None:
    """Creates 'log' dir and configures the logging behavior"""
    params = Params()
    os.makedirs(params.log_dir, exist_ok=True)
    fmt = (
            '%(asctime)s %(levelname)s: %(message)s\n"'
            '%(filename)s, %(funcName)s, %(lineno)s'
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


def _is_positive(x: int) -> bool:
    """Evaluates if 'x' is postive"""
    if x > 0:
        return True
    else:
        return False


def _validate_zoom_inputs(
        im: ndarray,
        width: int,
        height: int,
        x_offset: int,
        y_offset: int,
        ) -> None:
    """Evaluates the validity of zoom inputs.
    Raise:
        ValidationError: raised if an input is invalid
    """
    if not isinstance(im, ndarray):
        raise ValidationError(f"'im' must be a numpy ndarray, not {type(im)}.")

    if not im.ndim == 3:
        raise ValidationError("'im' must be a 3d ndarray.")

    if not _is_positive(x_offset):
        raise ValidationError("'x_offset' has to be positive")

    if not _is_positive(y_offset):
        raise ValidationError("'y_offset' has to be positive")

    if not _is_positive(width):
        raise ValidationError("'width' has to be positive")

    if not _is_positive(height):
        raise ValidationError("'height' has to be positive")

    if not (im.dtype == "uint8"
            or im.dtype == "uint32"
            or im.dtype == "uint64"):
        msg = f"Image's pixel must be type uint8/32/64, not {im.dtype}"
        raise ValidationError(msg)


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


def _grey_out_img(im: ndarray) -> ndarray:
    """Returns a grey scale image tensor."""
    len_x = im.shape[0]
    len_y = im.shape[1]

    grey_im = np.ones([len_x, len_y, 1], dtype="uint64")
    for i in range(len_x):
        for j in range(len_y):
            grey_px = _compute_px_luminance(im[i][j])
            grey_im[i][j] = grey_px
    return grey_im


def _display_image(im: np.ndarray) -> None:
    """Displays the image tensor with plt"""
    plt.imshow(im, cmap="grey")
    plt.show()


def _print(im: ndarray) -> None:
    """Outputs shape and tensor after slicing"""
    shape = im.shape
    print("New shape after slicing:", shape)
    print(im)
    return


# -------------------- Pub. methods --------------------
def zoom(
        im: ndarray,
        width: int,
        height: int,
        x_offset: int,
        y_offset: int
        ) -> ndarray:
    """Crops and greys out the image"""
    _validate_zoom_inputs(
        im=im,
        width=width,
        height=height,
        x_offset=x_offset,
        y_offset=y_offset
    )
    im = _grey_out_img(im)
    im = im[x_offset:x_offset + height, y_offset:y_offset + width]
    _print(im)
    return im


# -------------------- Main -----------------------------
def main():
    """loads, greys out and crops images"""
    try:
        params = Params()
        _setup_logging()
        logger = _get_logger()

        logger.info("Program '%s' started", params.script_name)
        logger.info("Loading image %s", params.img_path)

        im = ft_load(params.img_path)
        if im is None:
            raise ValidationError("Image couldn't be loaded")

        logger.info("Cropping image %s", params.img_path)
        im = zoom(im, width=400, height=400, x_offset=100, y_offset=450)

        _display_image(im)
    except ValidationError as e:
        logger.error("%s", e)
        exit(1)

    except Exception:
        logger.exception("Unexpected error")
        exit(1)

    logger.info("Program finished with success !")
    return


if __name__ == "__main__":
    main()
