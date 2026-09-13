# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set() #A list might be a better approach since there is nothing that says we cant have duplicate node values
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

        #This solution loops through curr and adds each node to a set, then if the node has already been seen we can return true meaning there is a cycle because the node has already been visited
        