
import pytest
from parking_lot.helpers.range_dict import RangeDict


@pytest.fixture
def valid_range_dict():
    valid_dict = RangeDict({range(0, 4): "foo", range(4, 8): "bar"})
    return valid_dict


def test_range_dict_get(valid_range_dict):
    assert valid_range_dict[1] == "foo"
    assert valid_range_dict[5] == "bar"
