"""functions for traversal of binary tree"""
class Node:
    """created new class"""
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    """pre_order"""
    if node is None:
        return []
    res = [node.data]
    left = pre_order(node.left)
    right = pre_order(node.right)
    res.extend(left)
    res.extend(right)
    return res

def in_order(node):
    """in order"""
    if node is None:
        return []
    res = []
    left = in_order(node.left)
    res.extend(left)
    res.append(node.data)
    right = in_order(node.right)
    res.extend(right)
    return res


def post_order(node):
    """post order"""
    if node is None:
        return []
    res = []
    left = post_order(node.left)
    res.extend(left)
    right = post_order(node.right)
    res.extend(right)
    res.append(node.data)
    return res

