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
                self.assertEqual(solution.isAlphabeticPalindrome(s), expected)

    def test_single_character(self):
        self._execute_test("Z", True)

    def test_lowercase_with_numbers(self):
        self._execute_test("abc123cba", True)

    def test_non_palindrome(self):
        self._execute_test("abc123", False)

    def test_classic_phrase_mixed_case_and_punctuation(self):
        self._execute_test("A man, a plan, a canal: Panama", True)

    def test_case_insensitive_matching(self):
        # 'A' matches 'a', 'b' matches 'B'
        self._execute_test("AbBa", True)

    def test_empty_string(self):
        # An empty string is symmetrically identical to itself
        self._execute_test("", True)

    def test_only_non_letters_numbers(self):
        # Filters completely to "", which is a valid palindrome
        self._execute_test("1234321", True)

    def test_only_non_letters_symbols(self):
        # Filters completely to "", which is a valid palindrome
        self._execute_test("!@#$%^&*()_+", True)

    def test_almost_palindrome_mismatch_at_edges(self):
        # Catches lazy pointer increments or bounds tracking issues
        self._execute_test("abcdecba", False)

    def test_single_letter_extracted_from_digits(self):
        # Digits drop, leaving "a", which is a valid single-letter palindrome
        self._execute_test("a123", True)


if __name__ == "__main__":
    unittest.main()
