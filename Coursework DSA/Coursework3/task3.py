class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


# -------- HELPER FUNCTIONS --------
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


# -------- USER INPUT --------
if __name__ == "__main__":
    sol = Solution()
    
    print("Enter elements of first linked list (space separated):")
    l1_vals = list(map(int, input().split()))
    
    print("Enter elements of second linked list (space separated):")
    l2_vals = list(map(int, input().split()))
    
    l1 = build_linked_list(l1_vals)
    l2 = build_linked_list(l2_vals)
    
    result = sol.addTwoNumbers(l1, l2)
    
    print("Output:")
    print_linked_list(result)