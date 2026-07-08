class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixes = [0] * n
        suffixes = [0] * n
        total_area = 0

        #prefixes
        for i in range(1, n):
            value = height[i - 1]
            prefixes[i] = max(prefixes[i - 1], value)

        #suffixes
        for i in range(n - 2, -1, -1):
            value = height[i + 1]
            suffixes[i] = max(suffixes[i + 1], value)

        for index, value in enumerate(height):
            min_height = min(prefixes[index], suffixes[index])
            if (min_height > value):
                total_area += (min_height - value)
            
        return total_area
                