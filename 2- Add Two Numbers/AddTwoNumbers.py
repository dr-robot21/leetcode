class ListNode :
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next
        



def addTwoNumbers(l1 : ListNode , l2 : ListNode) -> ListNode :
    rslt = l1
    prev = None
    val1 = val2 = carry = sum = 0
    
    while l1 or l2 or carry:
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry
        
        carry = sum // 10
        
        if l1 is not None:
            l1.val = sum % 10
        else:
            l1 = ListNode(sum%10)
            prev.next = l1
        
        prev = l1
        l1 = l1.next
        
        if l2: l2 = l2.next
        
    return rslt
            
            
            
            
def build_list(arr : list[int]) -> ListNode:
    first = ListNode(arr[0])
    current = first
    for item in arr[1:] :
        current.next = ListNode(item)
        current = current.next
        
    return first


def display_list(list : ListNode ) :
    current = list
    while current:
        print(current.val)
        current = current.next
        
    
    
l1 = build_list([9,9,9,9,9])
l2 = build_list([9,9,9])

l3 = addTwoNumbers(l1,l2)
display_list(l3)