class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than right element,
            # minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If mid element is less than or equal to right element,
                # minimum is in the left half (including mid)
                right = mid
        
        return nums[left]
        