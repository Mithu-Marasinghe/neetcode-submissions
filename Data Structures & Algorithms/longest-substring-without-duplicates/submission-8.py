class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_length = 0
        values = set()

        while r < len(s):
            if s[r] in values:
                while s[l] != s[r]:
                    values.remove(s[l])
                    l += 1
                values.remove(s[l])
                l += 1
            else:
                values.add(s[r])
                max_length = max(max_length, len(values))
                r += 1
        return max_length