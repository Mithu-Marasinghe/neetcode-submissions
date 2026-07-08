class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')':'(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if (c not in mp):
                stack.append(c)
            else:
                if ((stack) and (stack[-1] == mp[c])):
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True