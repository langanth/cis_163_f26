from character import *
from pytest import *

def test_character_default():
    c = Character()
    assert c.name == 'John Halo'
    assert c.health == 100
    assert c.temp_health == 100

print('check')