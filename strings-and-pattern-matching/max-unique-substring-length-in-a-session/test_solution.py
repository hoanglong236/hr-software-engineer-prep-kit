import unittest
from solution_s0 import Solution as SolutionS0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solutions = [
            SolutionS0(),
        ]

    def _execute_test(self, s, expected):
        """Helper to iterate through all solutions and apply test logic."""
        for solution in self.solutions:
            with self.subTest(impl=solution.__class__.__name__):
                self.assertEqual(
                    solution.maxDistinctSubstringLengthInSessions(s), expected
                )

    def test_sample_case(self):
        self._execute_test("abcabcbb", 3)

    def test_empty_string(self):
        self._execute_test("", 0)

    def test_all_unique_characters(self):
        self._execute_test("abcdefg", 7)

    def test_all_same_characters(self):
        self._execute_test("aaaaaa", 1)

    def test_include_asterisk(self):
        self._execute_test("abc*de", 3)

    def test_only_asterisks(self):
        self._execute_test("****", 0)

    def test_mixed_characters(self):
        self._execute_test("a*b*c*d*e", 1)

    def test_duplicate_within_segmented_session(self):
        # Session 1: "abcb" -> max unique is "abc" (3)
        # Session 2: "xyz" -> max unique is "xyz" (3)
        self._execute_test("abcb*xyz", 3)


if __name__ == "__main__":
    unittest.main()
