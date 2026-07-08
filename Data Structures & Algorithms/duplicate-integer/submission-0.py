class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        current_nums = set()
        for num in nums:
            if num in current_nums:
                return True
            else:
                current_nums.add(num)
        return False
        