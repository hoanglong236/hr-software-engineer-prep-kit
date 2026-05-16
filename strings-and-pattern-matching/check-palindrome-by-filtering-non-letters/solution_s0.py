class Solution:

    #
    # Complete the 'isAlphabeticPalindrome' function below.
    #
    # The function is expected to return a BOOLEAN.
    # The function accepts STRING code as parameter.
    #
    def isAlphabeticPalindrome(self, code):
        l, r = 0, len(code) - 1
        while l < r:
            while not code[l].isalpha() and l < r:
                l += 1
            while not code[r].isalpha() and r > l:
                r -= 1

            if code[l].lower() != code[r].lower():
                return False
            l += 1
            r -= 1
        return True