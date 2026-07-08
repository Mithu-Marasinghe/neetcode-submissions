class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in store:
                return [store[target - num], i]
            store[num] = i