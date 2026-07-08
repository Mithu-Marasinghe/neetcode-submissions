class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        result = []
        for r in range(k - 1, len(nums)):
            result.append(max(nums[l:r + 1]))
            l += 1
        
        return result