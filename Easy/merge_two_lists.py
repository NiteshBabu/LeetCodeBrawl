'''

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


'''

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
 
  temp = ListNode(float('-inf'))
  head = temp 
 
  while l1 and l2:
    if l1.val <= l2.val: 
      temp.next = l1
      l1 = l1.next 
    else: 
      temp.next = l2
      l2 = l2.next 
    temp = temp.next        
  
  if l1 : temp.next = l1
  else  : temp.next = l2
  
  return head.next


x = {
  '1':1,
  2:2
}

print(x.get(0, 'Not Found'))