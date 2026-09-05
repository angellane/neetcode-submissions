# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        if not head:
            return head

        while curr:
            nxt = curr.next
            curr.next = prev #because we are reversing we want the next node to current to be the previous node
            prev = curr #then prev has to become curr as we work down the list
            curr = nxt #because we made curr.next = prev, this would translate to curr = prev which isnt correct as we still need to work down the rest of the list. So we make a NXT variable which hold the next node of the current node, 

        return prev

        


        
