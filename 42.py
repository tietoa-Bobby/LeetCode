class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        # Initialize pointers and max height trackers
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        # Loop until the two pointers meet
        while left < right:
            # The amount of trapped water is limited by the shorter of the two max walls.
            if height[left] < height[right]:
                # Process the left side
                if height[left] >= left_max:
                    # This bar is a new or equal max, so it can't trap water. Update left_max.
                    left_max = height[left]
                else:
                    # This bar is shorter than left_max, so it traps water.
                    total_water += left_max - height[left]
                left += 1
            else:
                # Process the right side
                if height[right] >= right_max:
                    # This bar is a new or equal max, so it can't trap water. Update right_max.
                    right_max = height[right]
                else:
                    # This bar is shorter than right_max, so it traps water.
                    total_water += right_max - height[right]
                right -= 1
        
        return total_water