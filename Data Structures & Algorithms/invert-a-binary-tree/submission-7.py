# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left #this works due to tuple unpacking. The pairs are assigned at the same time effectively, meaning there is no need for a temp variable and the assignment happens at the same time ish?!?!
        self.invertTree(root.left)
        self.invertTree(root.right) #recursive dfs approach, root.left and right become 'root' on each recursive call
        return root        