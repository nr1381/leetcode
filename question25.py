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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        if k == 0:
            return head

        output = ListNode()   
        point = output
        before_head = None
        i = 1
        history = []
        while head != None:
            history.append(head.val)
            if i % k == 0:
                for h in reversed(range(len(history))):
                    point.val = history[h]
                    if h != 0 or head.next != None:
                        point.next = ListNode()
                        point = point.next
                history.clear()
            head = head.next
            i += 1
        if (i-1) % k != 0:
            for h in range(len(history)):
                point.val = history[h]
                if h != len(history)-1:
                    point.next = ListNode()
                    point = point.next
        return output


if __name__ == '__main__':
    head = [1,2,3,4]
    k = 3
    solution = Solution()
    input_node = ListNode().createListNode(head)
    output_node = solution.reverseKGroup(input_node, k)
    while output_node != None:
        print(output_node.val)
        output_node = output_node.next
