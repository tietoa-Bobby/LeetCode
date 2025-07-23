import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each number.
        # O(N) time where N is the length of nums.
        # e.g., nums = [1,1,1,2,2,3] -> counts = {1: 3, 2: 2, 3: 1}
        counts = collections.Counter(nums)

        # Step 2: Use a bucket sort approach.
        # The index of the list represents the frequency.
        # The size is len(nums) + 1 because a number can appear at most len(nums) times.
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        # Step 3: Collect the results from the buckets.
        # Iterate from the highest frequency to the lowest.
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result