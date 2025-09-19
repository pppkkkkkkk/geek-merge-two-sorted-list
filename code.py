'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        
        dummy = Node(-1)
        curr = dummy
        while head1 and head2:
            if head1.data > head2.data:
                curr.next = Node(head2.data)
                head2 = head2.next
            else:
                curr.next = Node(head1.data)
                head1 = head1.next
            curr = curr.next
        
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2
            
        return dummy.next
        
            