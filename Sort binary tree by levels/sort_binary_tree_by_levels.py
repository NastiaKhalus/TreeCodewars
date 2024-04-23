"""sorting binary tree"""
import collections
class Node:
    """created new class"""
    def __init__(self, L=None, R=None, n=None):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    """sorting tree"""
    if root is None:
        return []
    res = []
    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    while queue :
        node = queue.popleft()
        if node:
            res.append(node.value)
        if node.left and node.left not in visited:
            visited.add(node.left)
            queue.append(node.left)
        if node.right and node.right not in visited:
            visited.add(node.right)
            queue.append(node.right)
    return res

