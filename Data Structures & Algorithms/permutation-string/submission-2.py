class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l = 0
        r = len(s1) - 1
        s1_mp, s2_mp = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_mp[ord(s1[i]) - ord('a')] += 1
            s2_mp[ord(s2[i]) - ord('a')] += 1
        
        if s2_mp == s1_mp:
                return True

        for r in range(len(s1), len(s2)):
            if s2_mp == s1_mp:
                return True
            print(s1_mp, s2_mp)
            index1 = ord(s2[r]) - ord('a')
            index2 = ord(s2[l]) - ord('a')
            s2_mp[index2] -= 1
            s2_mp[index1] += 1

            if s2_mp == s1_mp:
                return True

            l += 1
        
        return False
