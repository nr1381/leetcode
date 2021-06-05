# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def createListNode(self, input_data=[]):
        if input_data == []:
            return None
        output = ListNode()
        point = output
        for i in range(len(input_data)):
            point.val = input_data[i]
            if i == len(input_data)-1:
                break
            point.next = ListNode()
            point = point.next
        return output

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        output = ListNode()   
        point = output
        before_head = None
        i = 1
        while head != None:
            if i % 2 == 0:
                point.val = head.val
                point.next = ListNode()
                point.next.val = before_head.val
                if head.next != None:
                    point.next.next = ListNode()
                    point = point.next.next
            else:
                before_head = head
            head = head.next
            i += 1
        if i % 2 == 0:
            point.val = before_head.val
        return output


if __name__ == '__main__':
    head = []
    solution = Solution()
    input_node = ListNode().createListNode(head)
    output_node = solution.swapPairs(input_node)
    while output_node != None:
        print(output_node.val)
        output_node = output_node.next
