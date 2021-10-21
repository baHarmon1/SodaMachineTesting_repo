class TestGetInventorySoda(unittest.TestCase):
    """Test the get_inventory_soda method in the SodaMachine class"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_pass_cola_return_soda_name_cola(self):
        """Test by passing in cola, and return the correct name"""
        cola_test = self.soda_machine.get_inventory_soda("Cola")
        self.assertEqual(cola_test.name, "Cola")

    def test_pass_orange_soda_return_soda_name_orange_soda(self):
        """Test be passing in orange_soda, and return the correct name"""
        orange_soda_test = self.soda_machine.get_inventory_soda("Orange Soda")
        self.assertEqual(orange_soda_test.name, "Orange Soda")

    def test_pass_rootbeer_return_soda_name_rootbeer(self):
        """Test be passing in rootbeer, and return the correct name"""
        rootbeer_test = self.soda_machine.get_inventory_soda("Root Beer")
        self.assertEqual(rootbeer_test.name, "Root Beer")

    def test_pass_incorrect_string_return_none(self):
        """Test by passing an incorrect string through get_inventory_soda, and return None"""
        incorrect_test = self.soda_machine.get_inventory_soda("Mountain dew")
        self.assertEqual(incorrect_test, None)


class TestReturnInventory(unittest.TestCase):
    """Test the return_inventory method of the SodaMachine class"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_pass_can_return_updated_list(self):
        """Test by instantiating and passing a can through the return_inventory and return an updated list"""
        cola_1 = Cola()
        self.soda_machine.return_inventory(cola_1)
        returned_list = len(self.soda_machine.inventory)
        self.assertEqual(returned_list, 31)


class TestDepositCoinsIntoRegister(unittest.TestCase):
    """Test deposit_coins_into_register method in the SodaMachine class"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_pass_list_of_each_coin_return_92(self):
        """Test by creating a list with each coin in it, then passing the list and getting a return of of 92"""
        list_of_each_coin = []
        quarter_1 = Quarter()
        dime_1 = Dime()
        nickel_1 = Nickel()
        penny_1 = Penny()
        list_of_each_coin.append(quarter_1)
        list_of_each_coin.append(dime_1)
        list_of_each_coin.append(nickel_1)
        list_of_each_coin.append(penny_1)
        self.soda_machine.deposit_coins_into_register(list_of_each_coin)
        passed_coins = len(self.soda_machine.register)
        self.assertEqual(passed_coins, 92)


if __name__ == "__main__":
    unittest.main()
