class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -=1
                elif total < 0:
                    l += 1
                else:
                    res.append((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return list(set(res))
            