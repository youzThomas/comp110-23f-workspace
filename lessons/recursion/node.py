"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute of the first element."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        if self.next is None:
            return None
        else:
            return Node(self.next.data, self.next.next)
    
    def last(self) -> int:
        """Return the `data` of the last element in the linked list."""
        now = self
        while now.next:
            now = now.next
        return now.data