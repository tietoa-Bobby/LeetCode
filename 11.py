class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize pointers at the beginning and end of the array.
        left, right = 0, len(height) - 1
        max_area = 0

        # Loop until the pointers meet.
        while left < right:
            # Calculate the width of the container.
            width = right - left
            
            # The height of the container is limited by the shorter of the two lines.
            h = min(height[left], height[right])
            
            # Calculate the current area and update max_area if it's larger.
            current_area = width * h
            max_area = max(max_area, current_area)

            # Move the pointer that points to the shorter line.
            # This is the key insight: moving the shorter line's pointer is the only
            # way to potentially increase the area, as we trade a smaller width
            # for a possibly larger height.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area