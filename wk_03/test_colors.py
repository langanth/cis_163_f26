from colors import Color
import pytest


@pytest.fixture
def valid_values():
    return ((0,125,255),(0,125,255),(0,125,255))

def test_default_color():
    c = Color()
    assert c.red == 0
    assert c.blue == 0
    assert c.green == 0

def test_color():
    red = (0, 255, 75, 125)
    blue = (0, 255, 75, 125)
    green = (0, 255, 75, 125)
    for i in range(len(red)):
        c = Color(red[i], green[i], blue[i])
        assert c.red == red[i]
        assert c.green == green[i]
        assert c.blue == blue[i]

@pytest.mark.parametrize("red,green,blue",((0,125,255),(0,125,255),(0,125,255)))
def test_color_alt(red, green, blue):
    c = Color(red, green, blue)
    assert c.red == red
    assert c.green == green
    assert c.blue == blue

@pytest.mark.parametrize('red', (-1, 256, -3, 3000))
def test_red_invalid_setter(red):
    with pytest.raises(ValueError):
        c = Color(red, 0, 0)

@pytest.mark.parametrize('red', (-1, 256, -3, 3000))
def test_red_invalid_setter(red):
    c = Color(0, 0, 0)
    with pytest.raises(ValueError):
        c.red = red

@pytest.mark.parametrize('red', ([], '3', 3.145))
def test_red_invalid__type(red):
    with pytest.raises(TypeError):
        c = Color(red, 0, 0)

@pytest.mark.parametrize('red', ([], '3', 3.145))
def test_red_invalid_setter_type(red):
    c = Color(0, 0, 0)
    with pytest.raises(TypeError):
        c.red = red