# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]


        while stack:
            nodeP, nodeQ = stack.pop()

            if not nodeP and not nodeQ:
                continue

            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            
            stack.append((nodeP.left, nodeQ.left))
            stack.append((nodeP.right, nodeQ.right))

        return True 


#3 Methods used to solve this problem
#1. Recursive DFS
#2. Iterative DFS
#3. BFS
        