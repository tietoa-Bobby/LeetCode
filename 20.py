class Solution(object):
    def isValid(self, s):
        # Dictionary to map closing brackets to opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        # Stack to hold opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the element from the stack if it's non-empty; otherwise use a dummy value
                top_element = stack.pop() if stack else "#"
                # Check if the mapping for teh closing bracket matches the top element
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push onto the stack
                stack.append(char)
            
        # If the stack is empty, all brackets were matched; otherwise some were unmatched
        return not stack