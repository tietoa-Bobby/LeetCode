class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        # The stack will store tuples of (index, height) for bars in increasing height order.
        stack = []  

        # We iterate through a modified heights list that includes a sentinel 0 at the end.
        # This ensures all bars in the original list are processed and popped from the stack.
        for i, h in enumerate(heights + [0]):
            # While the stack is not empty and the current bar is shorter than or equal to
            # the bar at the top of the stack, we can calculate the area for the popped bar.
            while stack and stack[-1][1] >= h:
                # Pop the bar from the stack.
                height = stack[-1][1]
                stack.pop()
                
                # Determine the width of the rectangle.
                # The right boundary is the current index 'i'.
                # The left boundary is the index of the new top of the stack.
                # If the stack is empty, the rectangle extends all the way to the beginning.
                width = i if not stack else i - stack[-1][0] - 1
                
                # Update the maximum area found so far.
                max_area = max(max_area, height * width)
            
            # Push the current bar's (index, height) onto the stack.
            stack.append((i, h))
            
        return max_area