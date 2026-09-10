# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ##splitting the linked list
        slow = head
        fast = head.next

        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next
        

        ##reversing the linked list
        curr = slow.next
        prev = slow.next = None 
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        ##putting back together

        first = head
        second = prev

        

        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        


        
