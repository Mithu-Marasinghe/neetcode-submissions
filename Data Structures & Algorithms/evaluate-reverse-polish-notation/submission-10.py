class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token in operands:
                val1 = stack.pop()
                val2 = stack.pop()
                match token:
                    case "+":
                        stack.append(val1 + val2)
                    case "*":
                        stack.append(val2 * val1)
                    case "-":
                        stack.append(val2 - val1)
                    case "/":
                        stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        return stack[0]