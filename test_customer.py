from logging import currentframe
import unittest
from customer import Customer


class TestGetWalletCoin(unittest.TestCase):
    """Test the get_wallet_coin method in Customer class"""

    def setUp(self):
        self.customer = Customer()
# Testing coin value

    def test_quarter_string_returns_quarter_instance(self):
        """Test that passing in "Quarter" returns a quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(.25, returned_coin.value)

    def test_dime_string_returns_dime_instance(self):
        """Test that passing in "Dime" returns a dime object"""
        returned_coin = self.customer.get_wallet_coin("Dime")
        self.assertEqual(.10, returned_coin.value)

    def test_nickel_string_returns_nickel_instance(self):
        """Test that passing in "Nickel" returns a nickel object"""
        returned_coin = self.customer.get_wallet_coin("Nickel")
        self.assertEqual(.05, returned_coin.value)

    def test_penny_string_returns_penny_instance(self):
        """Test that passing in "Penny" returns a penny object"""
        returned_coin = self.customer.get_wallet_coin("Penny")
        self.assertEqual(.01, returned_coin.value)
# Testing invalid strings

    def test_invalid_quarter_string_returns_none(self):
        """Test that passing an invalid quarter string should return none"""
        invalid_quarter_return = self.customer.get_wallet_coin("Invalid")
        self.assertIsNone(invalid_quarter_return)

    def test_invalid_dime_string_returns_none(self):
        """Test that passing an invalid dime string should return none"""
        invalid_dime_return = self.customer.get_wallet_coin("Invalid")
        self.assertIsNone(invalid_dime_return)

    def test_invalid_nickel_string_returns_none(self):
        """Test that passing an invalid nickel string should return none"""
        invalid_nickel_return = self.customer.get_wallet_coin("Invalid")
        self.assertIsNone(invalid_nickel_return)

    def test_invalid_penny_string_returns_none(self):
        """Test that passing an invalid penny string should return none"""
        invalid_penny_return = self.customer.get_wallet_coin("Invalid")
        self.assertIsNone(invalid_penny_return)


class TestAddCoinsToWallet(unittest.TestCase):
    """Test add_coins_to_wallet method in the Customer class"""

    def setUp(self):
        self.customer = Customer()

    def test_pass_list_of_coins_returns_valid_wallet(self):
        """Test add_coins_to_wallet by passing a string and checking that wallet is updated"""
        three_coins = ["Quarter", "Quarter", "Quarter"]
        self.customer.add_coins_to_wallet(three_coins)
        money_plus_three = len(self.customer.wallet.money)
        self.assertEqual(money_plus_three, 91)

    def test_pass_empty_list_return_no_change(self):
        """Test by passing an empty list, then verify there was no change to the wallet"""
        empty_list = []
        self.customer.add_coins_to_wallet(empty_list)
        added_empty_list = len(self.customer.wallet.money)
        self.assertEqual(added_empty_list, 88)


class AddCanToBackpack(unittest.TestCase):
    """Test add_can_to_backpack method in Customer class"""

    def setUp(self):
        self.customer = Customer()

    def test_add_can_to_backpack_returns_additional_value(self):
        """Test by adding a Cola object to customers backpack, then verify the value has been added"""
        self.customer.add_can_to_backpack("Cola")
        added_cola_to_backpack = len(self.customer.backpack.purchased_cans)
        self.assertEqual(added_cola_to_backpack, 1)


if __name__ == "__main__":
    unittest.main()
