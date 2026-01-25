from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def insert(l,h):
        if l > h:
            return None
        
        mid = (l + h) // 2
        root = TreeNode(nums[mid])
        root.left = insert(l , mid - 1)
        root.right = insert(mid + 1 , h)
        return root
    
    return insert(0,len(nums) - 1)