import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_length(self):
        """Test that you have 88 coins in your wallet."""
        wallet_length = len(self.wallet.money)
        self.assertEqual(88, wallet_length)

    if __name__ == "__main__":
        unittest.main()