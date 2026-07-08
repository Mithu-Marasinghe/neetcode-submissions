class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        sorted_keys = sorted(countMap.items(), key=lambda x: x[1], reverse=True)[:k]

        final_list = []
        for (val, count) in sorted_keys:
            final_list.append(val)

        return final_list

