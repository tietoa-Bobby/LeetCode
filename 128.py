class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Create a set for O(1) lookups.
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # This is the crucial optimization: only check for sequences
            # starting from numbers that don't have a smaller consecutive number.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the sequence starting from `num`.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)

        return longest_streak