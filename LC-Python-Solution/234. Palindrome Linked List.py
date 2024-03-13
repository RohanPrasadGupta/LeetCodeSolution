# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverseSecHalf(head):
            prev = None
            current = head
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev
            
        # first get the half of list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second reverse the second half as slow point to 2nd half onward
        revSecHalf = reverseSecHalf(slow)

        # now check if they are palindrome or not
        firstHalf =  head
        while revSecHalf:
            if revSecHalf.val != firstHalf.val:
                return False
            
            revSecHalf = revSecHalf.next
            firstHalf = firstHalf.next
        
        return True

        
        
        


        