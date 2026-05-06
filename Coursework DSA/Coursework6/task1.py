class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def build_list(arr):
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def removeNodes(head):
    head = reverse(head)

    max_val = head.val
    curr = head

    while curr and curr.next:
        if curr.next.val < max_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_val = curr.val

    return reverse(head)


# ---- USER INPUT ----
print("Enter the values of the linked list (space separated):")
arr = list(map(int, input().split()))

head = build_list(arr)
head = removeNodes(head)

print_list(head)