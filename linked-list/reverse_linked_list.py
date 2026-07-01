# Day 19 - Reverse Linked List
# LeetCode #206

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Helper — list se LinkedList banao
def make_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for n in nums[1:]:
        curr.next = ListNode(n)
        curr = curr.next
    return head

# Helper — LinkedList print karo
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test
print_list(reverse_list(make_list([1,2,3,4,5])))  # [5,4,3,2,1]
print_list(reverse_list(make_list([1,2])))         # [2,1]
print_list(reverse_list(make_list([])))            # []