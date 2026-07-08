class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '*', '-', '/'])
        operands_stack = []
        operators_stack = []
        print(tokens)
        for token in tokens:
            print(token)
            if token not in operators:
                operands_stack.append(int(token))
            else:
                val1 = operands_stack.pop()
                val2 = operands_stack.pop()
                answer = 0
                if (token == '+'):
                    answer = val1 + val2
                elif (token == '-'):
                    answer = val2 - val1
                elif (token == '*'):
                    answer = val1 * val2
                elif (token == '/'):
                    answer = int(val2 / val1)
                operands_stack.append(answer)
            print(operands_stack)
        print(operands_stack)
        return operands_stack[0]

            
            