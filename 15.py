class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to enable the two-pointer approach and handle duplicates easily.
        nums.sort()
        result = []
        n = len(nums)

        # Iterate through the array. The last possible first element is at index n-3.
        for i in range(n - 2):
            # Optimization: If the current number is positive, no subsequent triplet can sum to 0.
            if nums[i] > 0:
                break
            
            # Skip duplicate first elements to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Use two pointers for the rest of the array.
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    # The sum is too small, need a larger number.
                    left += 1
                elif current_sum > 0:
                    # The sum is too large, need a smaller number.
                    right -= 1
                else:
                    # Found a triplet that sums to zero.
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate second elements.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate third elements.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers to the next unique elements.
                    left += 1
                    right -= 1
        
        return result