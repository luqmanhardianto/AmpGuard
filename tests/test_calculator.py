import unittest

from calculator import (
    apply_safety_factor,
    calculate_single_phase_current,
    calculate_three_phase_current,
    calculate_current_method
)

class TestCurrentMethod(unittest.TestCase):
    def test_motor_current_method(self):
        inputs = {
            "load_type":"motor",
            "current":10
        }

        result = calculate_current_method(inputs)

        self.assertEqual(result, 12.5)

    def test_welding_current_method(self):
        inputs = {
            "load_type":"welding",
            "current":10
        }

        result = calculate_current_method(inputs)

        self.assertEqual(result, 20)

class TestSafetyFactor(unittest.TestCase):
    def test_motor_safety_factor(self):
        result = apply_safety_factor(
            current=10,
            safety_factor=1.25
        )

        self.assertEqual(result,12.5)

    def test_welding_safety_factor(self):
        result = apply_safety_factor(
            current=10,
            safety_factor=2
        )

        self.assertEqual(result, 20)

class TestSinglePhaseCurrent(unittest.TestCase):
    def test_single_phase_current(self):
        result = calculate_single_phase_current(
            power=2200,
            voltage=220,
            power_factor=1
        )

        self.assertEqual(result, 10)

class TestThreePhaseCurrent(unittest.TestCase):
    def test_three_phase_current(self):
        result = calculate_three_phase_current(
            power=3800,
            voltage=380,
            power_factor=1
        )

        self.assertAlmostEqual(result, 5.774, places=3)

if __name__ == "__main__":
    unittest.main()