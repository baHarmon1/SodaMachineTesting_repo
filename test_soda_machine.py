import unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_filled(self):
        """Test that the soda machine register has a list of size 88"""
        register_length = len(self.soda_machine.register)
        self.assertEqual(88, register_length)


class TestFillInventory(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()


if __name__ == "__main__":
    unittest.main()
