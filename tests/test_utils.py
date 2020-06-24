import pytest
import numpy as np

from translater import utils, timeit
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



