import unittest

import exercise.reinforcement as reinforcement

class TestReinforcement(unittest.TestCase):
    # R-1.1
    def test_is_multiple(self):
        self.assertTrue(reinforcement.is_multiple(5,10))

    # R-1.2
    def test_is_even(self):
        self.assertTrue(reinforcement.is_even(22))

    # R-1.3
    def test_min_max(self):
        self.assertEqual(reinforcement.min_max([2,1,35,4]), (1, 35))

    # R-1.4
    def test_sum_squares(self):
        self.assertEqual(reinforcement.sum_squares(5), 30)

    # R-1.5
    def test_sum_alter(self):
        self.assertEqual(reinforcement.sum_alter(5), 30)

    # R-1.6
    def test_sum_odd(self):
        self.assertEqual(reinforcement.sum_odd(6), 35)
        self.assertEqual(reinforcement.sum_odd(5), 10)

    # R-1.7
    def test_sum_odd_alter(self):
        self.assertEqual(reinforcement.sum_odd_alter(6), 35)
        self.assertEqual(reinforcement.sum_odd_alter(5), 10)

    # R-1.11
    def test_target_list(self):
        self.assertEqual(reinforcement.target_list(9), [1, 2, 4, 8, 16, 32, 64, 128, 256])

    # R-1.12
    def test_choice_emulator(self):
        self.assertIn(reinforcement.choice_emulator("welcome"), ('w','e','l','c','o','m','e'))


if __name__ == "__main__":
    unittest.main()
