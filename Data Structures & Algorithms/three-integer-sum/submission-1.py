class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(list(nums))
        result_set = set()
        for i in range(len(numbers) - 2):
            j = i + 1
            k = len(numbers) - 1
            required_value = - numbers[i]

            while (j < k):
                if (numbers[j] + numbers[k] < required_value):
                    j += 1
                elif (numbers[j] + numbers[k] > required_value):
                    k -= 1
                else:
                    result_set.add((numbers[i], numbers[j], numbers[k]))
                    j += 1
                    k -= 1

        result = []
        for val in result_set:
            result.append(list(val))

        return result

        