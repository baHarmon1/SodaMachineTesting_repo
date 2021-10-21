import unittest
from soda_machine import SodaMachine
import coins


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
        
class TestRegisterHasCoin(unittest.TestCase):

    def setUp(self):
        self.has_coin = SodaMachine()

    def test_register_has_quarters(self):
        """Tests that 'Quarter' type can be returned from register"""
        coin_type = self.has_coin.register_has_coin("Quarter")
        self.assertTrue(coin_type)

    def test_register_has_dimes(self):
        """Tests that 'Dime' type can be returned from register"""
        coin_type = self.has_coin.register_has_coin("Dime")
        self.assertTrue(coin_type)

    def test_register_has_nickel(self):
        """Tests that 'Nickel' type can be returned from register"""
        coin_type = self.has_coin.register_has_coin("Nickel")
        self.assertTrue(coin_type)

    def test_register_has_pennies(self):
        """Tests that 'Penny' type can be returned from register"""
        coin_type = self.has_coin.register_has_coin("Penny")
        self.assertTrue(coin_type)

    def test_fake_coin(self):
        """Tests that a 'non-valid' coin name cannot be returned from register"""
        coin_type = self.has_coin.register_has_coin("Invalid")
        self.assertFalse(coin_type)

class TestDetermineChangeValue(unittest.TestCase):
    """Test types of coins that can be returned from the register"""

    def setUp(self):
        self.value = SodaMachine()

    def test_higher_total_payment(self):
        higher_payment = self.value.determine_change_value(20,5)
        self.assertEqual(15, higher_payment)

    def test_higher_soda_price(self):
        higher_soda = self.value.determine_change_value(5,20)
        self.assertEqual(-15,higher_soda)

    def test_two_equal_values(self):
        equal_values = self.value.determine_change_value(10,10)
        self.assertEqual(0, equal_values)

class TestCalculateCoinValue(unittest.TestCase):
    """Test calculates the values of coins in a list"""

    def setUp(self):
        self.coin_value = SodaMachine()

    def test_calculate_coins_value(self):
        quarter_1 = coins.Quarter()
        dime_1 = coins.Dime()
        nickel_1 = coins.Nickel()
        penny_1 = coins.Penny()
        coin_list = []
        coin_list.append(quarter_1)
        coin_list.append(dime_1)
        coin_list.append(nickel_1)
        coin_list.append(penny_1)
        total_value = self.coin_value.calculate_coin_value(coin_list)
        self.assertEqual(.41, total_value)




if __name__ == "__main__":
    unittest.main()