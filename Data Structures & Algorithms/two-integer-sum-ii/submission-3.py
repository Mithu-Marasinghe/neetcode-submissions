class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            val1 = numbers[l]
            val2 = numbers[r]
            if (val1 + val2) < target:
                l += 1
            elif (val1 + val2) > target:
                r -= 1
            else:
                print(val1 + val2)
                return [l + 1, r + 1]
            