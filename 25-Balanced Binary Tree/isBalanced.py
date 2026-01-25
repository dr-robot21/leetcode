from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    rslt = True
    
    def maxDepth(node):
        nonlocal rslt 
        
        if not node:
            return 0
        
        l = maxDepth(node.left)
        r = maxDepth(node.right)
        
        if abs(l - r) > 1:
            rslt = False
        return 1 + max(l,r)
    
    maxDepth(root)
    
    return rslt