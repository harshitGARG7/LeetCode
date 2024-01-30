class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                integer2 = stack.pop()
                integer1 = stack.pop()
                Operator = token
                if Operator == '+':
                    resolved_ans= integer1 + integer2
                elif Operator == '-':
                    resolved_ans= integer1 - integer2
                elif Operator == '*':
                    resolved_ans= integer1 * integer2
                else:
                    resolved_ans= int(integer1 / integer2)
                stack.append(resolved_ans)
            else:
                stack.append(int(token))
        return stack.pop()
