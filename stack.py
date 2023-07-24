from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class Stack:
    def __init__(self, length, head):
        self.length = length
        self.head: Optional[Node] = head

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

    def pop(self, item):
        if self.head is not None:
            self.head.next = None
        self.length = self.length - 1
