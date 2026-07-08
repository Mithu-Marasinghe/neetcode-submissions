class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while (l < r):
            middle = math.floor((l + r) / 2)
            hours = 0
            for val in piles:
                hours += math.ceil(val / middle)
            
            if (hours <= h):
                r = middle
            else:
                l = middle + 1
        return r