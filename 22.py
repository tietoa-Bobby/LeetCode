class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # This list will store all the valid combinations.
        result = []

        # We use a backtracking function to build the combinations.
        # s: the current string being built
        # open_count: the number of open parentheses used so far
        # close_count: the number of close parentheses used so far
        def backtrack(s, open_count, close_count):
            # Base case: If the string has reached the desired length (2 * n),
            # it's a valid combination, so we add it to our result list.
            if len(s) == 2 * n:
                result.append(s)
                return

            # Recursive step 1: Add an open parenthesis if we can.
            # We can add an open parenthesis as long as we haven't used all 'n' of them.
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)

            # Recursive step 2: Add a close parenthesis if it's valid.
            # We can add a close parenthesis only if the number of close parentheses
            # is less than the number of open parentheses. This ensures well-formedness.
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        # Initial call to the backtracking function to start the process.
        backtrack("", 0, 0)
        return result