import unittest
from character import *

class TestCharacter(unittest.TestCase):

    def test_default__character(self):
        c = Character()
        self.assertEqual('John Halo', c.name, 'Incorrect Name')
        self.assertEqual(100, c.health, "Incorrect Health")
        self.assertEqual(100, c.temp_health, "Incorrect Temporary Health")

    def test_character_name(self):
        c = Character('Mario Mario')
        self.assertEqual('Mario Mario', c.name, "Incorrect name provided")



if __name__ == "__main__":
    unittest.main()