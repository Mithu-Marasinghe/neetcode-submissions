class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')':'(',
            '}': '{',
            ']': '['
        }

        stack = []
        for c in s:
            if c in mp.values():
                stack.append(c)
            else:
                if (not stack):
                    return False
                res = stack.pop()
                if res != mp[c]:
                    return False

        if stack:
            return False
        return True
