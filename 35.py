class Solution(object):
    def searchInsert(self, nums, target):
        return self.binary_search(nums, target)
    def binary_search(self, nums, target):
        bottom = 0
        top = len(nums) - 1
        temp = 0
        
        while bottom <= top:
            mid = (bottom + top) // 2
            if nums[mid]>target:
                top = mid-1
                
            elif nums[mid]<target:
                bottom = mid+1
                
            else:
                return mid
        else:
            return bottom

        