from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    rslt = []
    inOrder(root,rslt)
    return rslt



def inOrder(root: Optional[TreeNode],rslt: List[int]):
    if root:
        inOrder(root.left,rslt)
        rslt.append(root.val)
        inOrder(root.right,rslt)