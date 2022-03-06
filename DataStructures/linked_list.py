'''
Some Linked list functions
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode) -> ListNode:
    if not head: return
    prev, curr = None, head
    while curr and curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def removeElements(head: ListNode, val: int) -> ListNode:
    ''' Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
    '''
    if not head: return
    while head and head.val == val: # deal with first element
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            # if statement deals with last element
            curr.next = curr.next.next if curr.next else None
        else:
            curr = curr.next
    return head




def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    ''' Merge 2 sorted linked lists and return head
    '''
    if not list1 or not list2:
        return list1 or list2

    if list1.val <= list2.val:
        head = list1
        list1 = list1.val
    else:
        head = list2
        list2 = list2.val
    
    curr = head
    # step through each node and update
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    # if there is still a list that is left
    if list1 or list2:
        curr.next = list1 if list2 else list2
    return head