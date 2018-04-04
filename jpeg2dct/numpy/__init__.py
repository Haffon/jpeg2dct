import numpy as np
import os

from . import dctfromjpg_wrapper


def load(filename, normalized=True, channels=3):
    """
    read/load the dct coefficients from a jpg file
    :param filename: the jpg file name
    :param normalized: boolean. If True, dct coefficients are normalized with quantification tables. If False, no normalization is performed.
    :param channels: number of color channels for the decoded image
    :return: (dct_y, dct_c, dct_r) as numpy arrays of size h x w x nb dct coef
    :note: given an image of size 512 x 512 x 64, the dct_y will be 64 x 64 x 64 and dct_c, dct_r will be 32 x 32 x 64
    """
    if not os.path.exists(filename):
        raise IOError('{} does not exists'.format(filename))
    if channels not in {3, 1}:
        raise ValueError('channels should be 3 or 1')
    [band1, band2, band3] = dctfromjpg_wrapper.read_dct_coefficients_from_file(filename, normalized, channels)
    return [band1, band2, band3] if channels == 3 else [band1]


def loads(buffer, normalized=True, channels=3):
    """
    read/load the dct coefficients from a string of bytes representing a jpeg image
    :param buffer: the jpg file buffer
    :param normalized: boolean. If True, dct coefficients are normalized with quantification tables. If False, no normalization is performed.
    :param channels: number of color channels for the decoded image
    :return: (dct_y, dct_c, dct_r) as numpy arrays of size h x w x nb dct coef
    :note: given an image of size 512 x 512 x 64, the dct_y will be 64 x 64 x 64 and dct_c, dct_r will be 32 x 32 x 64
    """
    if channels not in {3, 1}:
        raise ValueError('channels should be 3 or 1')
    l_buffer = int(len(buffer))
    [band1, band2, band3] = dctfromjpg_wrapper.read_dct_coefficients_from_buffer(buffer, l_buffer, normalized, channels)
    return [band1, band2, band3] if channels == 3 else [band1]