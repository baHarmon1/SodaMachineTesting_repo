from os import DirEntry
import unittest
from cans import Can, Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel, Penny

from user_interface import display_payment_value, get_unique_can_names, try_parse_int, validate_main_menu


class TestValidateMainMenu(unittest.TestCase):
    """Test validate_main_menu method in the UserInterface class"""

    def test_pass_1_through_main_menu(self):
        """Test by passing 1 inside of the validate_main_menu method and returning (True, 1)"""
        test_input_1 = validate_main_menu(1)
        self.assertEqual(test_input_1, (True, 1))

    def test_pass_2_through_main_menu(self):
        """Test by passing 2 inside of the validate_main_menu method and returning (True, 2)"""
        test_input_2 = validate_main_menu(2)
        self.assertEqual(test_input_2, (True, 2))

    def test_pass_3_through_main_menu(self):
        """Test by passing 3 inside of the validate_main_menu method and returning (True, 3)"""
        test_input_3 = validate_main_menu(3)
        self.assertEqual(test_input_3, (True, 3))

    def test_pass_4_through_main_menu(self):
        """Test by passing 4 inside of the validate_main_menu method and returning (True, 4)"""
        test_input_4 = validate_main_menu(4)
        self.assertEqual(test_input_4, (True, 4))

    def test_pass_incorrect_number_through_main_menu(self):
        """Test by passing an incorrect number through main menu and return (False, None)"""
        test_input_incorrect = validate_main_menu(99)
        self.assertEqual(test_input_incorrect, (False, None))


class TestTryParseInt(unittest.TestCase):
    """Test try_parse_int method in UserInterface class"""

    def test_pass_string_10_return_int_10(self):
        """Test by passing the string of "10" to try_parse_int and return an int of 10"""
        pass_string_10 = try_parse_int("10")
        self.assertEqual(pass_string_10, 10)

    def test_pass_incorrect_string_return_0_int(self):
        """Test by passing an incorrect string with expected return int 0"""
        pass_incorrect_string = try_parse_int("Hello")
        self.assertEqual(pass_incorrect_string, 0)


class TestGetUniqueCanNames(unittest.TestCase):
    """Test the get_unique_can_names method in the UserInterface class"""

    def test_pass_multiple_cans_return_only_original_names(self):
        """Test get_unique_can_names by passing 2 of each cans to this function and checking that the list only has 3 names"""
        list_of_sodas = []
        cola_1 = Cola()
        cola_2 = Cola()
        orange_soda_1 = OrangeSoda()
        orange_soda_2 = OrangeSoda()
        rootbeer_1 = RootBeer()
        rootbeer_2 = RootBeer()
        list_of_sodas.append(cola_1)
        list_of_sodas.append(cola_2)
        list_of_sodas.append(orange_soda_1)
        list_of_sodas.append(orange_soda_2)
        list_of_sodas.append(rootbeer_1)
        list_of_sodas.append(rootbeer_2)
        passed_list = len(get_unique_can_names(list_of_sodas))
        self.assertEqual(passed_list, 3)

    def test_pass_empty_list(self):
        """Test by passing empty list into get_unique_can_names and expected return is an empty list"""
        list_of_sodas = []
        passed_list = len(get_unique_can_names(list_of_sodas))
        self.assertEqual(passed_list, 0)


class TestDisplayPaymentValue(unittest.TestCase):
    """Test display_payment_value method in UnitInterface Class"""

    def test_each_coins_value(self):
        """Test each coins value by passing in all of the coins and returning the total value"""
        list_of_coins = []
        quarter_1 = Quarter()
        dime_1 = Dime()
        nickel_1 = Nickel()
        penny_1 = Penny()
        list_of_coins.append(quarter_1)
        list_of_coins.append(dime_1)
        list_of_coins.append(nickel_1)
        list_of_coins.append(penny_1)
        total_value = display_payment_value(list_of_coins)
        self.assertEqual(total_value, .41)

    def test_passing_an_empty_string(self):
        """Test by passing an empty string and returned value is 0"""
        list_of_coins = []
        total_value = display_payment_value(list_of_coins)
        self.assertEqual(total_value, 0)


if __name__ == "__main__":
    unittest.main()
