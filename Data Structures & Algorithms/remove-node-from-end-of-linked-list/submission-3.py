# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # initialises the dummy node value to be 0 and the next pointer to be at the head
        left = dummy 
        right = head 

        while n > 0 and right: # this is used to make the right pointer moved n spaces from the left. 
            right = right.next
            n -= 1
         
        while right: #while right isnt null, so right hasnt reached the end of the list yet, we increment
            left = left.next
            right = right.next

        left.next = left.next.next # breaks the link, effectively deletes the node at n 
        return dummy.next #returns everything in the list after dummy
        