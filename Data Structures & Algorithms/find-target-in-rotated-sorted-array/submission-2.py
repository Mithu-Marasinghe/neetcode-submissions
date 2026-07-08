class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l < r):
            print(l, r)
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
            
        if target >= nums[pivot] and target <= nums[-1]:
            new_l = pivot
            new_r = len(nums) - 1
        else:
            new_l = 0
            new_r = pivot
        
        while (new_l <= new_r):
            mid = (new_l + new_r) // 2
            if (target < nums[mid]):
                new_r = mid - 1
            elif (target > nums[mid]):
                new_l = mid + 1
            else:
                return mid
        return -1
                