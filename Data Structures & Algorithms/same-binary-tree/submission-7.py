# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#3 Methods used to solve this problem
#1. Recursive DFS - Sets conditions and uses recursion on the function - No dfs function is created to preserve space, but it can also be created

#2. Iterative DFS - Uses a stack with the pair p and q. While the stack is not empty it pops p and q from the stack where their values are stores in respective nodes. Then conditions are ran on the nodes and their children are appended to the stack.

#3. BFS - Uses 2 queues (deque in this case, acts the same way as a queue or stack depending on how you want to use it), While the queues are not empty you run a loop on the size of the queue. At the root it is only one, Then you can pop the roots from each queue and store their values in respective nodes, you then set the conditions and then append the children of the nodes to the stack where the loop executes again until you have popped all nodes.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = deque([[p,q]])


        while stack:
            nodeP, nodeQ = stack.pop()

            if not nodeP and not nodeQ:
                continue

            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            
            stack.append((nodeP.left, nodeQ.left))
            stack.append((nodeP.right, nodeQ.right))

        return True 



        