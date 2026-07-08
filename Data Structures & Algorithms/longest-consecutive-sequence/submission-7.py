class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return 1
        n = sorted(nums)
        print(n)
        length = 1
        curr_length = 0
        for i in range(1, len(n)):
            print(i, curr_length, length)
            if n[i] == n[i - 1] + 1:
                curr_length += 1
            elif n[i] == n[i - 1]:
                continue
            else:
                print(f"Not greater at {i}")
                curr_length = 0
            length = max(length, curr_length + 1)
        return length