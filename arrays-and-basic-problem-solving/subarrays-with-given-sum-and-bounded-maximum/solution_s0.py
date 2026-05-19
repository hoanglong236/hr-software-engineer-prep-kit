class Solution:

    #
    # Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
    #
    # The function is expected to return a LONG_INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER_ARRAY nums
    #  2. LONG_INTEGER k
    #  3. LONG_INTEGER M
    #
    def countSubarraysWithSumAndMaxAtMost(self, nums, k, M):
        ans = 0
        running_sum = 0
        sum_map = {0: 1}

        for num in nums:
            if num > M:
                running_sum = 0
                sum_map = {0: 1}
            else:
                running_sum += num
                ans += sum_map.get(running_sum - k, 0)
                sum_map[running_sum] = sum_map.get(running_sum, 0) + 1
        return ans
