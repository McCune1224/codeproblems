# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head

        while curr.next:
            print(curr.val)
            curr = curr.next


        return head



if __name__ == "__main__":
    pass
