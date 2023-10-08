from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)  # Node to be added

        if self.head is None:  # An empty list
            self.head = new
        else:  # Non-empty ==> Find last node
            node = self.head  # and attach new node as last

            # Loops through all nodes in deque and finds the last node
            while node.nxt is not None:
                node = node.nxt  # Move to next node
            node.nxt = new  # connect the new node to the last node

        self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # Add element n as first entry in deque
    def add_first(self, n):
        # set the new node the the head and the new node to connect to that one
        new = Node(n, None)  # Node to be added
        if self.head is None:  # An empty list
            self.head = new
        else:  # Non-empty ==> Find last node
            new = Node(n, self.head)  # Node to be added

        self.head = new
        self.size += 1

        # handle tail
        node = self.head
        past_node = None

        # Loops through all nodes in deque and finds the last node
        while node.nxt is not None:
            node = node.nxt  # Move to next node
            past_node = node
        self.tail = past_node

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail is not None:
            return self.tail.value
        return None

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is not None:
            return self.head.value
        return None

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        node = self.head

        if self.head is not None:
            self.head = self.head.nxt
            self.size -= 1
            return node.value

        return None

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size == 0:
            print("deque is empty")
            return None

        # Handle one item case
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return None

        node = self.head
        prev_tail = self.tail
        while node.nxt is not None:
            if node.nxt is self.tail:
                node.nxt = None
                self.tail = node
                self.size -= 1
                return prev_tail.value

            node = node.nxt
