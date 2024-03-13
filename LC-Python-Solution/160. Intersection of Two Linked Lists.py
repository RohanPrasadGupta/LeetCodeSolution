# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def getLength(head):
            current = head
            length = 0
            while current:
                length+=1
                current = current.next
            return length

        lenA = getLength(headA)
        lenB = getLength(headB)

        diff = abs(lenA-lenB)

        if(lenA>lenB):
            for i in range(diff):
                headA = headA.next
        else:
            for i in range(diff):
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
            




        