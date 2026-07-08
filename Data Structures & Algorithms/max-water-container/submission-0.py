class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        result_area = 0
        while (i  < j):
            min_height = min(heights[i], heights[j])
            area = min_height * (j - i)
            result_area = max(result_area, area)

            if (min_height == heights[i]):
                i += 1
            else:
                j -= 1
        return result_area