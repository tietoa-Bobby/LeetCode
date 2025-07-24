class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize two pointers, one at the beginning and one at the end of the array.
        left, right = 0, len(numbers) - 1

        # Iterate until the two pointers meet.
        # The loop invariant is that the solution, if it exists, is between the pointers.
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # If the sum equals the target, we've found our pair.
                # The problem asks for 1-based indices, so we add 1 to each.
                return [left + 1, right + 1]
            elif current_sum < target:
                # If the sum is less than the target, we need a larger sum.
                # Since the array is sorted, moving the left pointer to the right
                # will increase the sum.
                left += 1
            else:  # current_sum > target
                # If the sum is greater than the target, we need a smaller sum.
                # Moving the right pointer to the left will decrease the sum.
                right -= 1