# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, count):
            nonlocal res
            

            if not node:
                return 
            
            #if there is no nodes with a value greater than prev
            if node.val >= count:
                res += 1
                count = node.val
            
            dfs(node.right, count)
            dfs(node.left, count)


            return


        dfs(root, 0)
        return res
            
            

                    