class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while (l < r):
            print(l, r)
            middle = math.floor((l + r) / 2)
            hours = 0
            for val in piles:
                hours += math.ceil(val / middle)
                print(f"{hours} after {val} with middle {middle} ")
            
            if (hours <= h):
                r = middle
            else:
                l = middle + 1
        print("FInal is")
        print(l, r)
        return r

        # 1 1.5 2 3 4
        #       ^
        # 2 - 4 hours
        # Range 1 - 2
        # Middle = 2