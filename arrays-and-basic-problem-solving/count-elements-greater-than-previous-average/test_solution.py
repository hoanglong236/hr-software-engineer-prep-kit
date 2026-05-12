import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, arr, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.countResponseTimeRegressions(arr), expected)

    def test_example_case(self):
        """Standard case with mixed fluctuations."""
        self._execute_test([100, 200, 150, 300], 2)

    def test_no_regression_on_constant_values(self):
        """A stable sequence (all equal) should result in zero regressions."""
        self._execute_test([5, 5, 5, 5], 0)

    def test_strict_increase_yields_maximum_regressions(self):
        """Every element in a strictly increasing sequence exceeds the previous average."""
        self._execute_test([1, 2, 3, 4, 5, 6], 5)

    def test_strict_decrease_yields_zero_regressions(self):
        """Elements in a strictly decreasing sequence never exceed the previous average."""
        self._execute_test([6, 5, 4, 3, 2, 1], 0)

    def test_fluctuating_values_with_stagnation(self):
        """Handles cases where values rise, fall, and repeat, creating a dynamic average."""
        self._execute_test([1, 3, 2, 2, 3], 2)

    def test_single_element_input(self):
        """Boundary Case: A single element has no 'previous' average to compare against."""
        self._execute_test([10], 0)

    def test_no_element_input(self):
        """Edge Case: An empty array should return zero regressions."""
        self._execute_test([], 0)

    def test_large_value_gap(self):
        """Edge Case: Ensure logic holds when an element is significantly larger than the average."""
        self._execute_test([1, 1, 1, 999999999], 1)


if __name__ == "__main__":
    unittest.main()
