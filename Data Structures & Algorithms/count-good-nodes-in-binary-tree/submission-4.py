# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, seen):
            nonlocal count
            if not root:
                return
            
            print(root.val, seen)
            if not seen or root.val >= max(seen):
                print("Added ")
                count += 1

            new_seen = {val for val in seen}
            new_seen.add(root.val)
            
            dfs(root.left, new_seen)
            dfs(root.right, new_seen)
        
        dfs(root, set())
        return count