class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


if __name__ == "__main__":
    sol = Solution()
    
    print("Enter elements of sorted linked list (space separated):")
    values = list(map(int, input().split()))
    
    head = build_linked_list(values)
    
    result = sol.deleteDuplicates(head)
    
    print("Output:")
    print_linked_list(result)