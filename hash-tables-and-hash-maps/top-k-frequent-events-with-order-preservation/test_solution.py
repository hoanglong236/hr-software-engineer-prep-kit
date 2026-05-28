import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, events, k, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(solution.getTopKFrequentEvents(events, k), expected)

    def test_sample_case_1(self):
        # Frequencies: 1: (3), 2: (2), 3: (1)
        self._execute_test(events=[1, 2, 1, 3, 2, 1], k=2, expected=[1, 2])

    def test_sample_case_2(self):
        # Frequencies: 2: (3), 4: (2), 1: (2), 3: (2)
        # Tie break: 4, 1, 3 all have frequency 2. 4 appeared first, then 1.
        self._execute_test(events=[4, 4, 1, 2, 2, 3, 1, 3, 2], k=3, expected=[2, 4, 1])

    def test_single_event(self):
        self._execute_test(events=[5], k=1, expected=[5])

    def test_empty_events(self):
        self._execute_test(events=[], k=0, expected=[])

    def test_all_events_same_frequency_k_equals_unique_count(self):
        self._execute_test(events=[1, 2, 3], k=3, expected=[1, 2, 3])

    def test_all_events_same_frequency_k_less_than_unique_count(self):
        self._execute_test(events=[1, 2, 3], k=2, expected=[1, 2])

    def test_multiple_events_same_frequency_preserves_first_appearance_order(self):
        # Frequencies are all 2. Insertion order of appearance: 1, then 2, then 3.
        self._execute_test(events=[1, 2, 2, 3, 3, 1], k=2, expected=[1, 2])

    def test_all_events_same_frequency_with_scrambled_insertion_order(self):
        # Frequencies are all 1. Stream is reversed to ensure no accidental numerical sorting.
        self._execute_test(events=[3, 2, 1], k=2, expected=[3, 2])


if __name__ == "__main__":
    unittest.main()
