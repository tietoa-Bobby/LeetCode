class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        # Initialize the result array with 0s.
        answer = [0] * n
        # The stack will store indices of the temperatures.
        stack = []

        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is warmer
            # than the temperature at the index on top of the stack.
            while stack and t > temperatures[stack[-1]]:
                # Pop the index of the previous, colder day.
                prev_index = stack.pop()
                # Calculate the difference in days and update the answer.
                answer[prev_index] = i - prev_index
            
            # Push the current index onto the stack.
            stack.append(i)
            
        return answer