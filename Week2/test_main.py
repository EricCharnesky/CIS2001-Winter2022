from unittest import TestCase
from main import SprayBottle

class TestSprayBottle(TestCase):
    def test_add_liquid_successful(self):
        # AAA

        # Arrange - setting up the variables we need to test with
        milliliters_to_add = 100
        expected_result = True
        bottle = SprayBottle(milliliters_to_add)

        # Act - calling the code we are testing
        actual_result = bottle.add_liquid(milliliters_to_add)

        # Assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test_add_liquid_fails_on_negative(self):
        # AAA

        # Arrange - setting up the variables we need to test with
        milliliters_to_add = -100
        expected_result = False
        bottle = SprayBottle(100)

        # Act - calling the code we are testing
        actual_result = bottle.add_liquid(milliliters_to_add)

        # Assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test_add_liquid_fails_on_overfill(self):
        # AAA

        # Arrange - setting up the variables we need to test with
        milliliters_to_add = 100
        expected_result = False
        bottle = SprayBottle(milliliters_to_add/2)

        # Act - calling the code we are testing
        actual_result = bottle.add_liquid(milliliters_to_add)

        # Assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)


    def test_spray_successful(self):
        # Arrange
        milliliters_to_spray = 10
        bottle = SprayBottle(10)
        bottle.add_liquid(10)
        expected_result = True

        # Act
        actual_result = bottle.spray(milliliters_to_spray)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_spray_failed_on_negative(self):
        # Arrange
        milliliters_to_spray = -10
        bottle = SprayBottle(10)
        bottle.add_liquid(10)
        expected_result = False

        # Act
        actual_result = bottle.spray(milliliters_to_spray)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_spray_failed_on_too_large_of_spray(self):
        # Arrange
        milliliters_to_spray = 100
        bottle = SprayBottle(10)
        bottle.add_liquid(10)
        expected_result = False

        # Act
        actual_result = bottle.spray(milliliters_to_spray)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_gets(self):
        # Arrange
        expected_current_volume_in_milliliters = 50
        expected_max_volume_in_milliliters = 100
        bottle = SprayBottle(expected_max_volume_in_milliliters)
        bottle.add_liquid(expected_current_volume_in_milliliters)

        # Act
        actual_current_volume_in_milliliters = bottle.get_current_volume_in_milliliters()
        actual_max_volume_in_milliliters = bottle.get_max_volume_in_milliliters()

        # Assert
        self.assertEqual(expected_current_volume_in_milliliters, actual_current_volume_in_milliliters)
        self.assertEqual(expected_max_volume_in_milliliters, actual_max_volume_in_milliliters)
