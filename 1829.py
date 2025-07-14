class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)
        max_val = (1 << maximumBit) - 1 # Maximum value with "maximumBit" bits
        total_xor = 0

        # Calc the initial XOR of all elements in nums
        for num in nums:
            total_xor ^= num
        answer = []
        # Process each query from end to start of nums
        for i in range(n - 1, -1, -1):
            # k to maximize XOR is total_xor XOR max_val
            answer.append(total_xor ^ max_val)
            # Remove last element effect from total_xor
            total_xor ^= nums[i]
        
        return answer