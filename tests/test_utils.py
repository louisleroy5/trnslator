import pytest

from translater import utils


def test_rotate(config):
    # Shift list elements to the left
    l1 = [1, 2, 3]  # list
    n = 1  # shift 1 position to the left
    l2 = utils.rotate(l1, n)

    assert (l2 == [2, 3, 1])






