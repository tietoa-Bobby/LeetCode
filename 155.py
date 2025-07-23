class MinStack(object):

    def __init__(self):
        """
        Initializes the stack object.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        Pushes the element val onto the stack.
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If the min_stack is empty or the new value is less than or equal to
        # the current minimum, push it onto the min_stack.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Removes the element on the top of the stack.
        :rtype: None
        """
        # If the element being popped is the current minimum, it must also be
        # popped from the min_stack to expose the next minimum.
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        Gets the top element of the stack.
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()