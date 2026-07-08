class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Have a hash set (key = num, value = set of all values above)
        # Loop once through it, if there is a bigger num, you add everything in
        #   the bigger nums set to the smaller num 
        if (len(nums)) == 0:
            return 0
            
        set_values = set()
        for num in nums:
            set_values.add(num)
        
        possible_starts = []
        for num in nums:
            if (num - 1) not in set_values:
                possible_starts.append(num)
        
        print(possible_starts)
        count = 1
        for start in possible_starts:
            temp_count = 1 
            while (start + 1) in set_values:
                temp_count += 1
                start += 1
            
            count = max(temp_count, count)
        return count
       
            
