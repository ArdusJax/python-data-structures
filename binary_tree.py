from typing import List, Optional
from collections import deque


class BinarySearchTree:
    def __init__(self):
        self.height = 0


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional[BinaryNode] = None
        self.right: Optional[BinaryNode] = None


def pre_order_traversal(curr: Optional[BinaryNode], path):
    if curr is None:
        return path
    # visitNode
    path.append(curr.value)
    # recurseL
    pre_order_traversal(curr.left, path)
    # recurseR
    pre_order_traversal(curr.right, path)
    return path


def in_order(curr: Optional[BinaryNode], path):
    if curr is None:
        return path
    # recurseL
    in_order(curr.left, path)
    # visitNode
    path.append(curr.value)
    # recurseR
    return


def post_order(curr: Optional[BinaryNode], path):
    if curr is None:
        return path
    # recurseL
    post_order(curr.left, path)
    # recurseR
    post_order(curr.right, path)
    # visitNode
    path.append(curr.value)

    return path


def walk(curr: BinaryNode, path):
    if curr is None:
        return path


def dfs(head: Optional[BinaryNode], needle):
    return search(head, needle)


def search(curr: Optional[BinaryNode], needle):
    if curr is None:
        return False

    if curr.value == needle:
        return True

    if curr.value < needle:
        return search(curr.right, needle)

    return search(curr.left, needle)


def bfs(head: Optional[BinaryNode], needle):
    if head is None:
        return False

    q = deque([head])

    while len(q):
        curr = q.popleft()

        if curr is None:
            continue

        if curr.value == needle:
            return True

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

        return False


def compare(a: Optional[BinaryNode], b: Optional[BinaryNode]):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


def insert(tree: Optional[BinaryNode], value):
    if tree is None:
        return
