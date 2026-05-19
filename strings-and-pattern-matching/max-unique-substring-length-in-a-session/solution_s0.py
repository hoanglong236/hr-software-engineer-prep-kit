class Solution:

    #
    # Complete the 'maxDistinctSubstringLengthInSessions' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING sessionString as parameter.
    #
    def maxDistinctSubstringLengthInSessions(self, sessionString):
        idx_dict = {}
        ans = 0
        pivot = 0
        for i, c in enumerate(sessionString):
            if c == "*":
                idx_dict = {}
                pivot = i + 1
                continue

            if c in idx_dict:
                pivot = max(pivot, idx_dict[c] + 1)

            distinct_len = i - pivot + 1
            if distinct_len > ans:
                ans = distinct_len
            idx_dict[c] = i
        return ans
