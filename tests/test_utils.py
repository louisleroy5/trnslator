import pytest
import os

import numpy as np

from translater import utils, timeit, settings
from geomeppy.geom.polygons import Polygon3D


def test_rotate(config):
    # Shift list elements to the left
    l1 = [1, 2, 3]  # list
    n = 1  # shift 1 position to the left
    l2 = utils.rotate(l1, n)

    assert l2 == [2, 3, 1]


@timeit
def test_lcm(config):
    # This function takes two integers and returns the L.C.M.
    x = 10
    y = 50
    lcm = utils.lcm(x, y)

    assert lcm == 5


def test_float_round(config):
    # Makes sure a variable is a float and round it at "n" decimals
    num = 40.24
    n = 1
    float_num = utils.float_round(num, n)

    assert float_num == 40.2


def test_angle(config):
    # Calculate the angle between 2 vectors
    # Polygon1 & vector1
    poly1 = Polygon3D(
        [(215.5, 5.0, 0.5), (215.5, 5.0, 2.0), (217.0, 5.0, 2.0), (217.0, 5.0, 0.5)]
    )
    v1 = poly1.normal_vector
    v2 = v1
    angle = utils.angle(v1, v2, acute=False)

    assert angle == 2 * np.pi


def test_write_lines(config):
    # Delete file if exists, then write lines in it
    path = settings.data_folder
    lines = ["Test to write lines in file", "2nd line", "end of document"]
    utils.write_lines(path, lines)

    assert os.path.exists(path)


def test_date_transform(config):
    # Simple function transforming one-based hours (1->24) into zero-based hours (0->23)
    date_str = "08:10"
    new_date = utils.date_transform(date_str)

    assert new_date == "07:10"
