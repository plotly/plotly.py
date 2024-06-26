import numpy as np
import base64

plotlyjsShortTypes = {
    "int8": "i1",
    "uint8": "u1",
    "int16": "i2",
    "uint16": "u2",
    "int32": "i4",
    "uint32": "u4",
    "float32": "f4",
    "float64": "f8",
}

int8min = -128
int8max = 127
int16min = -32768
int16max = 32767
int32min = -2147483648
int32max = 2147483647

uint8max = 255
uint16max = 65535
uint32max = 4294967295


def b64(v):
    """
    Convert numpy array to plotly.js typed array sepc
    If not possible return the original value
    """

    if not isinstance(v, np.ndarray):
        return v

    dtype = str(v.dtype)

    # convert default Big Ints until we could support them in plotly.js
    if dtype == "int64":
        max = v.max()
        min = v.min()
        if max <= int8max and min >= int8min:
            v = v.astype("int8")
        elif max <= int16max and min >= int16min:
            v = v.astype("int16")
        elif max <= int32max and min >= int32min:
            v = v.astype("int32")
        else:
            return v

    elif dtype == "uint64":
        max = v.max()
        min = v.min()
        if max <= uint8max and min >= 0:
            v = v.astype("uint8")
        elif max <= uint16max and min >= 0:
            v = v.astype("uint16")
        elif max <= uint32max and min >= 0:
            v = v.astype("uint32")
        else:
            return v

    dtype = str(v.dtype)

    if dtype in plotlyjsShortTypes:
        arrObj = {
            "dtype": plotlyjsShortTypes[dtype],
            "bdata": base64.b64encode(v).decode("ascii"),
        }

        if v.ndim > 1:
            arrObj["shape"] = str(v.shape)[1:-1]

        print(arrObj)

        return arrObj

    return v


def _b64(v):
    return b64(np.array(v))
