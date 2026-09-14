# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            for i in range(len(pq)):
                pNode = pq.popleft()
                qNode = qq.popleft()

                if pNode is None and qNode is None:
                    continue
                if pNode is None or qNode is None or pNode.val != qNode.val:
                    return False

                
                pq.append(pNode.left)
                pq.append(pNode.right)
                
                qq.append(qNode.left)
                qq.append(qNode.right)
        return True
            
            
            