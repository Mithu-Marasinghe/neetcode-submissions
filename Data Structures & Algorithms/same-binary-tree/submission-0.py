# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = True
        def check(p, q):
            nonlocal result
            if not p and not q:
                return 
            elif not p or not q or p.val != q.val:
                result = False
            else:
                check(p.left, q.left)
                check(p.right, q.right)

        check(p, q)
        return result
            
