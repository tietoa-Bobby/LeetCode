class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                # Pop the second operand first
                op2 = stack.pop()
                # Pop the first operand second
                op1 = stack.pop()

                if token == '+':
                    stack.append(op1 + op2)
                elif token == '-':
                    stack.append(op1 - op2)
                elif token == '*':
                    stack.append(op1 * op2)
                elif token == '/':
                    # Division truncates toward zero
                    stack.append(int(float(op1) / op2))
            else:
                # Token is a number, push it onto the stack
                stack.append(int(token))
        
        # The final result is the only element left on the stack
        return stack[0]