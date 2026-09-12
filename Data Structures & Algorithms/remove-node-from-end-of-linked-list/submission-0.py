# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#This is the first approach. Creating a an array and filling it with the linkedlist we can then count from the right of the array and then return the list, having removed that entry

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # we want to remove a node from the right that is n spaces from the right

        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            return head.next

        nxt = nodes[len(nodes) - n].next
        prev = nodes[len(nodes) - n - 1]
        prev.next = nxt



        return head

        #nodes[len(nodes) - n] This is the entry in the array we want to remove

        


        