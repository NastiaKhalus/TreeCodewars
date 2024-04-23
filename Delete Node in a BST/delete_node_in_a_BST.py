"""deleting a node"""
from typing import Optional

class TreeNode:
    """created new class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """created new class"""
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """deleting a node"""
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            else:
                n = root.right
                while n.left:
                    n = n.left
                root.val = n.val
                root.right = self.deleteNode(root.right, n.val)
        return root
