class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialise the answer array. The output array does not count as extra space.
        answer = [1] * n

        # --- First Pass: Calculate Prefix Products ---
        # At the end of this loop, answer[i] will contain the product of all
        # elements to the left of nums[i].
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # --- Second Pass: Calculate Suffix Products and Final Result ---
        # We iterate from right to left, calculating the suffix product on the fly.
        # We then multiply it by the prefix product already stored in answer[i].
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer