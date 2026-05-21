import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, taskDurations, slotLength, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(
                    solution.findTaskPairForSlot(taskDurations, slotLength), expected
                )

    def test_sample_case_match_found(self):
        """Standard case where a valid pair exists early in the sorted array."""
        self._execute_test(taskDurations=[2, 7, 11, 15], slotLength=9, expected=[0, 1])

    def test_sample_case_no_match(self):
        """Case where no combination of elements can reach the target slot length."""
        self._execute_test(taskDurations=[1, 2, 3, 4], slotLength=8, expected=[-1, -1])

    def test_duplicate_values_forming_target(self):
        """Identical values at the end of the array combine to match the target."""
        self._execute_test(taskDurations=[1, 2, 3, 4, 4], slotLength=8, expected=[3, 4])

    def test_any_combination_duplicate_pair(self):
        """Ensures any valid combination of duplicate values forming the target is accepted."""
        # Valid pairs that sum to 7:
        # index 1 & 3 (3+4), index 1 & 4 (3+4), index 2 & 3 (3+4), index 2 & 4 (3+4)
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                res = solution.findTaskPairForSlot(
                    taskDurations=[1, 3, 3, 4, 4], slotLength=7
                )
                # Check that we got two distinct indices and their values sum to 7
                self.assertEqual(len(res), 2)
                self.assertEqual(sum([1, 3, 3, 4, 4][i] for i in res), 7)

    def test_any_of_multiple_pairs_available(self):
        """Ensures any valid pair is accepted when multiple distinct pairs can sum to the target."""
        # Valid pairs that sum to 5: [0, 3] (1+4) OR [1, 2] (2+3)
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                res = solution.findTaskPairForSlot(
                    taskDurations=[1, 2, 3, 4, 5], slotLength=5
                )
                self.assertEqual(len(res), 2)
                self.assertEqual(sum([1, 2, 3, 4, 5][i] for i in res), 5)

    def test_prevents_matching_element_with_itself(self):
        """Ensures a single element equal to half the target cannot be reused twice."""
        # Target is 8. Element 4 exists at index 1.
        # If a nested loop forgets 'if i != j:', it will match index 1 with index 1 (4 + 4 = 8) and fail.
        self._execute_test(taskDurations=[1, 4, 2, 5], slotLength=8, expected=[-1, -1])

    def test_same_value_at_different_indices(self):
        """Target is exactly double an element value; requires two distinct indices."""
        self._execute_test(taskDurations=[3, 1, 3, 5], slotLength=6, expected=[0, 2])

    def test_empty_array(self):
        """Edge case with no tasks; should return no valid pair."""
        self._execute_test(taskDurations=[], slotLength=5, expected=[-1, -1])

    def test_one_element_array(self):
        """Edge case with only one task; cannot form a pair."""
        self._execute_test(taskDurations=[5], slotLength=5, expected=[-1, -1])

    def test_two_elements_array_valid_pair(self):
        """Edge case with exactly two tasks that sum to the target."""
        self._execute_test(taskDurations=[2, 3], slotLength=5, expected=[0, 1])

    def test_same_value_multiple_times(self):
        """Same value appears multiple times; should return the first valid pair of indices."""
        self._execute_test(taskDurations=[2, 2, 2, 2], slotLength=4, expected=[0, 1])


if __name__ == "__main__":
    unittest.main()
