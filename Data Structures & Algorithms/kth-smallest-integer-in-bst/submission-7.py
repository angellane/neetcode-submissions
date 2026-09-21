# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        q = deque([root])
        res = []

        while q:

            
            node = q.popleft()
            res.append(node.val)
            if node.right:
                res.append(node.right.val)
            if node.left:
                res.append(node.left.val)

        return res[k - 1]
