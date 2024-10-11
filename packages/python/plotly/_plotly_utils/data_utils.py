from io import BytesIO
import base64
from .png import Writer, from_array

try:
    from PIL import Image

    pil_imported = True
except ImportError:
    pil_imported = False


def image_array_to_data_uri(
    img, backend="pil", compression=4, ext="webp", backend_kwargs=None
):
    """Converts a numpy array of uint8 into a base64 png or jpg string.

    Parameters
    ----------
    img: ndarray of uint8
        array image
    backend: str
        'auto', 'pil' or 'pypng'. If 'auto', Pillow is used if installed,
        otherwise pypng.
    compression: int, between 0 and 9
        compression level to be passed to the backend
    ext: str, 'webp', 'png', or 'jpg'
        compression format used to generate b64 string
    backend_kwargs : dict or None
        keyword arguments to be passed to the backend
    """
    # PIL and pypng error messages are quite obscure so we catch invalid compression values
    if compression < 0 or compression > 9:
        raise ValueError("compression level must be between 0 and 9.")
    alpha = False
    if img.ndim == 2:
        mode = "L"
    elif img.ndim == 3 and img.shape[-1] == 3:
        mode = "RGB"
    elif img.ndim == 3 and img.shape[-1] == 4:
        mode = "RGBA"
        alpha = True
    else:
        raise ValueError("Invalid image shape")
    if backend == "auto":
        backend = "pil" if pil_imported else "pypng"
    if ext != "png" and backend != "pil":
        raise ValueError(
            "webp and jpg binary strings are only available with PIL backend"
        )

    if backend_kwargs is None:
        backend_kwargs = {}

    if backend == "pypng":
        backend_kwargs.setdefault("compression", compression)

        ndim = img.ndim
        sh = img.shape
        if ndim == 3:
            img = img.reshape((sh[0], sh[1] * sh[2]))
        w = Writer(
            sh[1],
            sh[0],
            greyscale=(ndim == 2),
            alpha=alpha,
            **backend_kwargs,
        )
        img_png = from_array(img, mode=mode)
        prefix = "data:image/png;base64,"
        with BytesIO() as stream:
            w.write(stream, img_png.rows)
            base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
    else:  # pil
        if ext == "png":
            backend_kwargs.setdefault("compress_level", compression)

        if ext == "webp":
            backend_kwargs.setdefault("lossless", True)

        if not pil_imported:
            raise ImportError(
                "pillow needs to be installed to use `backend='pil'. Please"
                "install pillow or use `backend='pypng'."
            )
        pil_img = Image.fromarray(img)
        if ext == "webp":
            prefix = "data:image/webp;base64,"
            ext = "webp"
        elif ext == "jpg" or ext == "jpeg":
            prefix = "data:image/jpeg;base64,"
            ext = "jpeg"
        else:
            prefix = "data:image/png;base64,"
            ext = "png"
        with BytesIO() as stream:
            pil_img.save(
                stream,
                format=ext,
                **backend_kwargs,
            )
            base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
    return base64_string
