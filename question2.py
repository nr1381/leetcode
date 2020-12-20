# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = str(l1.val)
        while True:
            if l1.next == None:
                break
            l1 = l1.next    
            node1 += str(l1.val)
        node2 = str(l2.val)
        while True:
            if l2.next == None:
                break
            l2 = l2.next    
            node2 += str(l2.val)
            
        ans_num_reverse = int(node1[::-1]) + int(node2[::-1])
 

        tmp = ListNode()
        ans = tmp
        i = 1
        for num in str(ans_num_reverse)[::-1]:
            tmp.val = num
            if i != len(str(ans_num_reverse)):
                tmp.next = ListNode()
                tmp = tmp.next
                i += 1
        return ans
