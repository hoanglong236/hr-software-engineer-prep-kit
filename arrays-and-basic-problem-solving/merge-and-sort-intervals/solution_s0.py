class Solution:

    #
    # Complete the 'mergeHighDefinitionIntervals' function below.
    #
    # The function is expected to return a 2D_INTEGER_ARRAY.
    # The function accepts 2D_INTEGER_ARRAY intervals as parameter.
    #
    def mergeHighDefinitionIntervals(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])
        return ans