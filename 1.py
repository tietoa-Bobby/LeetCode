class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers adn their indices
        num_to_index = {}
        # Iterate over the list with index
        for i, num in enumerate(nums):
            # Calculate complement
            complement = target - num
            # Check if the complment is already in teh dictionary
            if complement in num_to_index:
                # If found return the indicies of the two numbers
                return [num_to_index[complement], i]
            # Otherwise, add teh current number to the dictionary
            num_to_index[num] = i
