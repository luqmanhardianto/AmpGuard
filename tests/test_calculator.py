import unittest

from calculator import apply_safety_factor

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

if __name__ == "__main__":
    unittest.main()