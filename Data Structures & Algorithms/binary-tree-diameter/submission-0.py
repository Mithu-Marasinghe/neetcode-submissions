# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def recursiveDFS(root: Optional[TreeNode]) -> int:
            nonlocal maxDepth
            if not root:
                return 0

            left = recursiveDFS(root.left)
            right = recursiveDFS(root.right)

            maxDepth = max(maxDepth, left + right)
            return 1 + max(left, right)
        
        recursiveDFS(root)
        return maxDepth