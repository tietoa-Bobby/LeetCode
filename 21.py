# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to serve as teh start of teh merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and compare nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current= current.next # Move the pointer in the merged list

        # Attach the remaining nodes, if any
        current.next = list1 if list1 else list2

        # Return the head of the merged list, skipping the dummy node
        return dummy.next        