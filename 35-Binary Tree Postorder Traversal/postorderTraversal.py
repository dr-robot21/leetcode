from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    rslt = []
    if not root :
        return rslt
    
    stack = [root]
    while stack:
        root = stack.pop()
        rslt.append(root.val)
        
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
            
    return rslt[::-1]