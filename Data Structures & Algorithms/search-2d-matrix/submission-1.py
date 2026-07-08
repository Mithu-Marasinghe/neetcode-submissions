class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row
        l = 0
        r = len(matrix) - 1
        row = 0
        while (l <= r):
            middle = l + (r - l) // 2
            if (target < matrix[middle][0]):
                r = middle - 1
            elif (target > matrix[middle][-1]):
                l = middle + 1
            else:
                row = middle
                break
        
        # Find col
        l = 0
        r = len(matrix[0]) - 1
        row_list = matrix[row]
        while (l <= r):
            middle = l + (r - l) // 2
            if (target < row_list[middle]):
                r = middle - 1
            elif (target > row_list[middle]):
                l = middle + 1
            else: 
                return True
        return False
