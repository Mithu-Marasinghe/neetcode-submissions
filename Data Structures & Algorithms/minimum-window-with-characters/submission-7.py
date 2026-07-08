class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        l = 0
        t_mp = [0] * 58
        s_mp = [0] * 58
        matching = 0
        res = ""
        for r in range(len(t)):
            t_mp[ord(t[r]) - ord('A')] += 1


        for r in range(0, len(s)):
            # Add it
            
            s_count = s_mp[ord(s[r]) - ord('A')]
            t_count = t_mp[ord(s[r]) - ord('A')]
            print(s[r], s_count, t_count)
            if s_count < t_count:
                matching += 1
                
            print("Adding for " + s[r])
        
            s_mp[ord(s[r]) - ord('A')] += 1

            
            if matching == len(t):
                print("Matching is equal to length")
                print(r - l, len(res))
                # Pop until not matching by 1
                while matching == len(t):
                    if (not res) or (r - l < len(res)):
                        print("Updating res")
                        res = s[l:r+1]
                        print(res)
                    print("Peeking " + s[l])
                    if not s_mp[ord(s[l]) - ord('A')] > t_mp[ord(s[l]) - ord('A')]:
                        matching -= 1
                    s_mp[ord(s[l]) - ord('A')] -= 1
                    l += 1
                peeked = False
                while not peeked and l < len(s):
                    print("Removing " + s[l])
                    if not s_mp[ord(s[l]) - ord('A')] > t_mp[ord(s[l]) - ord('A')]:
                        peeked = True
                    else:
                        s_mp[ord(s[l]) - ord('A')] -= 1
                        l += 1
                    


        return res
