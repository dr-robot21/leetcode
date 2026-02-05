from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    p = headA
    p2 = headB
    while p != p2:
        p = p.next if p else headB
        p2 = p2.next if p2 else headA
    return p