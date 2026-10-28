from unittest import TestCase, main
from add import add

class TestAdd(TestCase):

    def test_good_add(self):
        x = add(2, 3)
        self.assertEquals(5, x)

    def test_bad_add(self):
        with self.assertRaises(ValueError):
            x = add(-1, 3)


if __name__ == "__main__":
    main()