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

    def test_inventory_length(self):
        inventory_length = len(self.soda_machine.inventory)
        self.assertEqual(30, inventory_length)

class TestGetCoinFromRegister(unittest.TestCase):

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_register_quarter(self):
        """Test that 'Quarter' can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual("Quarter", returned_coin.name)

    def test_get_coin_register_dime(self):
        """Test that 'Dime' can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual("Dime", returned_coin.name)

    def test_get_coin_register_nickle(self):
        """Test that 'Nickel' can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual("Nickel", returned_coin.name)

    def test_get_coin_register_penny(self):
        """Test that 'Penny' can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual("Penny", returned_coin.name)

    def test_passing_string(self):
        """Test the 'None' can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register("Invalid")
        self.assertIsNone(returned_coin)
        

if __name__ == "__main__":
    unittest.main()