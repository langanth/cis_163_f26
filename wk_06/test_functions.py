from functions import *
import pytest

def test_add_basic():
    assert add(1, 1) == 2

def test_add_data_types():
    with pytest.raises(TypeError):
        x = add('1', 1)

@pytest.mark.parametrize("a, b", ((1, 2), (3, 4), (5, 6)))
def test_add_params(a, b):
   assert add(a, b) > -1