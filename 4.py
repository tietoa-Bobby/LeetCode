class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Elements in left partition
        
        left, right = 0, m
        
        while left <= right:
            # Partition nums1 at position i
            i = (left + right) // 2
            # Partition nums2 at position j to ensure left partition has 'half' elements
            j = half - i
            
            # Get boundary elements
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]
            
            # Check if partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found correct partition
                if total % 2 == 1:
                    # Odd total length - median is max of left partition
                    return max(nums1_left, nums2_left)
                else:
                    # Even total length - median is average of max(left) and min(right)
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                # nums1 partition too far right, move left
                right = i - 1
            else:
                # nums1 partition too far left, move right
                left = i + 1
        
        # Should never reach here with valid input
        return 0.0
        