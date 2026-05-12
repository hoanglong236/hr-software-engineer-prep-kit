class Solution:

    #
    # Complete the 'countResponseTimeRegressions' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts INTEGER_ARRAY responseTimes as parameter.
    #
    def countResponseTimeRegressions(self, responseTimes):
        ans = 0
        if len(responseTimes) == 0:
            return ans

        total = responseTimes[0]
        for i in range(1, len(responseTimes)):
            if responseTimes[i] > total / i:
                ans += 1
            total += responseTimes[i]
        return ans
