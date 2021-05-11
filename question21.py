from typing import List

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        tmp_output = output
        i = 0
        j = 0
        while l1 != None or l2 != None:
            tmp_output.next = ListNode()
            tmp_output = tmp_output.next
            if l1 is None:
                tmp_output.val = l2.val
                l2 = l2.next
                continue
            if l2 is None:
                tmp_output.val = l1.val
                l1 = l1.next
                continue
            if l1.val <= l2.val:
                tmp_output.val = l1.val
                l1 = l1.next
            else:
                tmp_output.val = l2.val
                l2 = l2.next
        return output.next
            
        
            

if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    solution = Solution()
    print(solution.mergeTwoLists(l1, l2)) 
