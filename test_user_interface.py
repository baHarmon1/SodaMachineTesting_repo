import unittest

from user_interface import validate_main_menu


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


if __name__ == "__main__":
    unittest.main()
