class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair [temp, index]
        for index, value in enumerate(temperatures):
            print(index, value)
            if not stack:
                stack.append((value, index))
                # continue

            while (stack and stack[-1][0] < value):
                val, ind = stack.pop()
                res[ind] = index - ind
            
            stack.append((value, index))

            print(stack)
            print(res)
        return res