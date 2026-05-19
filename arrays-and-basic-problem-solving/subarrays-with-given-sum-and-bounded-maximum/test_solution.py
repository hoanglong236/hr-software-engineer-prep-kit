import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, nums, k, M, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(
                    solution.countSubarraysWithSumAndMaxAtMost(nums, k, M), expected
                )

    def test_example_case(self):
        self._execute_test(nums=[2, -1, 2, 1, -2, 3], k=3, M=2, expected=2)

    def test_empty_element(self):
        self._execute_test(nums=[], k=0, M=0, expected=0)

    def test_single_element(self):
        self._execute_test(nums=[5], k=5, M=5, expected=1)

    def test_sum_matches_but_violates_maximum_bound(self):
        # The subarray [5] sums to 5, but its maximum element (5) is GREATER than M=4.
        # Therefore, valid subarrays count should be 0.
        self._execute_test(nums=[5], k=5, M=4, expected=0)

    def test_multiple_valid_sliding_windows(self):
        # Target sum = 3, Max element in subarray <= 3.
        # Subarrays matching sum=3: [1, 2], [3], [2, 1]
        # Max checks: max([1,2])=2<=3 (Pass), max([3])=3<=3 (Pass), max([2,1])=2<=3 (Pass)
        self._execute_test(nums=[1, 2, 3, 2, 1], k=3, M=3, expected=3)

    def test_valid_sum_but_element_exceeds_maximum_internally(self):
        # Target sum = 4, Max element <= 3.
        # Subarrays matching sum=4: [1, 3] and [4]
        # [1, 3] -> max is 3 (Passes M <= 3)
        # [4] -> max is 4 (Fails M <= 3)
        self._execute_test(nums=[1, 3, 4], k=4, M=3, expected=1)

    def test_zeros_extending_valid_subarrays(self):
        # Zeros can alter the subarray count dramatically because they add to length without shifting the sum!
        # Target sum = 2, Max element <= 2.
        # Base valid subarray: [2]
        # With zeros: [2], [2, 0], [0, 2], [0, 2, 0]
        self._execute_test(nums=[0, 2, 0], k=2, M=2, expected=4)

    def test_include_negative_numbers(self):
        self._execute_test(nums=[1, -1, 2, -2], k=0, M=2, expected=3)


if __name__ == "__main__":
    unittest.main()
