class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        # Helper function to merge two lists
        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            current.next = l1 if l1 else l2
            return dummy.next
        
        # Step: Merge all lists one by one
        result = None
        for l in lists:
            result = merge(result, l)
        
        return result


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
    
    k = int(input("Enter number of linked lists: "))
    
    lists = []
    
    for i in range(k):
        print(f"Enter elements of list {i+1} (space separated, press Enter for empty list):")
        line = input().strip()
        
        if line == "":
            lists.append(None)
        else:
            values = list(map(int, line.split()))
            lists.append(build_linked_list(values))
    
    result = sol.mergeKLists(lists)
    
    print("Merged Linked List:")
    print_linked_list(result)