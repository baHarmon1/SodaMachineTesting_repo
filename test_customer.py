import unittest
from customer import Customer


class TestGetWalletCoin(unittest.TestCase):
    """Test got the get_wallet_coin method in Customer class"""

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


if __name__ == "__main__":
    unittest.main()
