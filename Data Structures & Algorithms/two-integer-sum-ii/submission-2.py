class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1

        while i < j:
            # print(f"Checking {numbers[i]} and {numbers[j]}")
            if (numbers[i] + numbers[j] > target):
                j -= 1
            else:
                if (numbers[i] + numbers[j] == target):
                    return [i + 1, j + 1]
                i += 1 
        return [0, 0]