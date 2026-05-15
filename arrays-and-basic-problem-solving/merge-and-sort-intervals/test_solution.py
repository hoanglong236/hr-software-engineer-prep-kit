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
                self.assertEqual(solution.mergeHighDefinitionIntervals(arr), expected)

    def test_example_case(self):
        self._execute_test(
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_overlapping_intervals(self):
        self._execute_test(
            [[1, 4], [2, 5], [7, 9]],
            [[1, 5], [7, 9]],
        )

    def test_contained_intervals(self):
        self._execute_test(
            [[1, 10], [2, 3], [4, 5]],
            [[1, 10]],
        )

    def test_non_overlapping_intervals(self):
        self._execute_test(
            [[1, 2], [3, 4], [5, 6]],
            [[1, 2], [3, 4], [5, 6]],
        )

    def test_unordered_intervals(self):
        self._execute_test(
            [[5, 6], [2, 4], [1, 3]],
            [[1, 4], [5, 6]],
        )

    def test_single_interval(self):
        self._execute_test(
            [[1, 5]],
            [[1, 5]],
        )

    def test_empty_input(self):
        self._execute_test(
            [],
            [],
        )

    def test_adjacent_intervals(self):
        self._execute_test(
            [[1, 2], [2, 3], [3, 4]],
            [[1, 4]],
        )

    def test_same_start_intervals(self):
        self._execute_test(
            [[1, 4], [1, 5], [1, 3]],
            [[1, 5]],
        )

    def test_same_end_intervals(self):
        self._execute_test(
            [[1, 4], [2, 4], [3, 4]],
            [[1, 4]],
        )

    def test_duplicate_intervals(self):
        self._execute_test(
            [[1, 3], [1, 3]],
            [[1, 3]],
        )


if __name__ == "__main__":
    unittest.main()
