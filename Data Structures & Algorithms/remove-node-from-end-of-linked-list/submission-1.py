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
            return head.next #for a list with only 1 node, head.next will always be None so the return will be empty. 

        nxt = nodes[len(nodes) - n].next #we find the value that the node want to remove points at 
        prev = nodes[len(nodes) - n - 1] #we find the value before the node we want to remove 
        prev.next = nxt #here where n would be we are removing that link by making the next value for the node before = to the node after n 



        return head

        #nodes[len(nodes) - n] This is the entry in the array we want to remove

        


        