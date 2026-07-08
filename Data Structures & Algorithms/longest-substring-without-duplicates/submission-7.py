class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (not s):
            return 0
            
        max_length = 1
        l = 0
        r = 0
        values = set()
        while r < len(s):
            if s[r] in values:
                max_length = max(max_length, len(values))
                while s[l] != s[r]:
                    values.remove(s[l])
                    l += 1
                values.remove(s[l])
                l += 1

            else:
                values.add(s[r])
                r += 1
        return max(max_length, len(values))


