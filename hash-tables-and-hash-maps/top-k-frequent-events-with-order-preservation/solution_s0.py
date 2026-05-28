class Solution:

    #
    # Complete the 'getTopKFrequentEvents' function below.
    #
    # The function is expected to return an INTEGER_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER_ARRAY events
    #  2. INTEGER k
    #
    def getTopKFrequentEvents(self, events, k):
        freq = {}
        first_appearance_map = {}
        for i, event in enumerate(events):
            if event not in first_appearance_map:
                first_appearance_map[event] = i
            freq[event] = freq.get(event, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], first_appearance_map[x[0]]))
        return [event for event, _ in sorted_freq[:k]]


if __name__ == "__main__":
    events = [1, 2, 1, 3, 2, 1]
    k = 2
    print(Solution().getTopKFrequentEvents(events, k))
