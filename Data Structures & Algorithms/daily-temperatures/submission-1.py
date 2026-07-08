class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            if not stack:
                stack.append((value, index))

            while (stack and stack[-1][0] < value):
                val, ind = stack.pop()
                res[ind] = index - ind
            
            stack.append((value, index))

        return res