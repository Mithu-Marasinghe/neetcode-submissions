class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while (l < r and not s[l].isalnum()):
                l += 1
            while (l < r and not s[r].isalnum()):
                r -= 1
            print(l, r)
            if s[l].upper() == s[r].upper():
                l += 1
                r -= 1
            else:
                print(s[l], s[r])
                return False

        return True