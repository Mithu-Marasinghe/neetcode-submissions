# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, curr_max):
            nonlocal count
            if not root:
                return
            
            if root.val >= curr_max:
                count += 1
            
            new_max = max(curr_max, root.val)
            dfs(root.left, new_max)
            dfs(root.right, new_max)
        
        dfs(root, float("-inf"))
        return count