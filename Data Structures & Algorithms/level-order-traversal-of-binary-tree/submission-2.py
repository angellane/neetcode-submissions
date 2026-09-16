# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#BFS, move through list counting levels and moving values from nodes that are on the same level to the same list 
#



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        q = deque([root])
        
        
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()        
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left.val) ######
                    if node.right:
                        q.append(node.left.val)#commented lines work for 1 iteration on the root node but fail after, because when they are added to the queue they are added as integer values already. Not as tree nodes, so when the next iteration runs it fails here because an integer doesnt have a val attribute
            res.append(level)
        return res





