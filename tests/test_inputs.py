# import module unittest
import unittest
# import patch
from unittest.mock import patch

# import ask_power_factor
from inputs import ask_power_factor

# class for testing input power factor
class TestPowerFactor(unittest.TestCase):
    
    @patch("builtins.input", return_value="0.8")
    def test_valid_power_factor(self, mock_input):
        result = ask_power_factor()

        self.assertEqual(result,0.8)

    @patch("builtins.input", return_value="1.2")
    def test_power_factor_above_one(self, mock_input):
        with patch("builtins.input", side_effect=["1.2","0.8"]):
            result = ask_power_factor()

        self.assertEqual(result, 0.8)

if __name__ == "__main__":
    unittest.main()
