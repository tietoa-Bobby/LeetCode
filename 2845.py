from collections import defaultdict

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        prefix_count = 0
        result = 0
        count_map = defaultdict(int)
        count_map[0] = 1


        for num in nums:
            if num % modulo == k:
                prefix_count += 1

            needed_prefix = (prefix_count - k) % modulo

            result += count_map[needed_prefix]

            count_map[prefix_count % modulo] += 1
        
        return result