class Solution:

    #
    # Complete the 'findTaskPairForSlot' function below.
    #
    # The function is expected to return an INTEGER_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER_ARRAY taskDurations
    #  2. INTEGER slotLength
    #
    def findTaskPairForSlot(self, taskDurations, slotLength):
        tracking = {}
        for i, v in enumerate(taskDurations):
            if slotLength - v in tracking:
                return [tracking[slotLength - v], i]
            tracking[v] = i
        return [-1, -1]
