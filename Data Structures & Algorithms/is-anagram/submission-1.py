class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Loop through the "s" and make a dict with every letter and its count
        # Loop through "t" and do the same
        # Check if the dicts are equal
        s_dict = {}
        for num in s:
            if num in s_dict:
                s_dict[num] += 1
            else:
                s_dict[num] = 1
        
        t_dict = {}
        for num in t:
            if num in t_dict:
                t_dict[num] += 1
            else:
                t_dict[num] = 1
        
        if s_dict == t_dict:
            return True
        
        return False
        