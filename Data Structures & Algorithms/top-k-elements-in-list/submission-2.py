class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = dict()
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        
        heap = []
        for num, value in frequency_map.items():
            heapq.heappush(heap, (value, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[-1])
        
        return res
