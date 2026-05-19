class SolutionS1:

    #
    # Complete the 'maxDistinctSubstringLengthInSessions' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts STRING sessionString as parameter.
    #
    def maxDistinctSubstringLengthInSessions(self, sessionString):
        ans = 0
        for string in sessionString.split("*"):
            if not string:
                continue

            indices = [-1] * 26
            window_size = 0
            for i, ch in enumerate(string):
                o = ord(ch) - ord("a")
                if indices[o] == -1 or i - indices[o] > window_size:
                    window_size += 1
                else:
                    ans = max(ans, window_size)
                    window_size = i - indices[o]
                indices[o] = i
            ans = max(ans, window_size)

        return ans
