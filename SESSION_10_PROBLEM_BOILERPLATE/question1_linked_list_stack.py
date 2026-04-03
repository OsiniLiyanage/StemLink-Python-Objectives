"""
============================================================
SESSION 10 - QUESTION 1: STACK USING A LINKED LIST
============================================================
Topics: Node class, pointer manipulation, Stack backed by linked list

Instructions:
- Implement a Stack using a linked list (NOT a Python list)
- The "top" of the stack is the head of the linked list
- Push = prepend (add at head), Pop = remove head
- Do NOT use a Python list (no self.items = [])
- Run this file to test your implementation
- Do NOT modify the test code at the bottom
============================================================
"""


class Node:
    """
    A single node in a linked list.

    Attributes:
        data: The value stored in this node
        next: Reference to the next node (or None if last)
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    A stack implemented using a linked list.

    The top of the stack is the head of the linked list.
    Push adds a node at the head, pop removes from the head.
    This gives true O(1) push and pop -- no resizing ever!

    Attributes:
        top: Reference to the top node (head of linked list)
        _size: Number of items in the stack
    """

    def __init__(self):
        """Initialize an empty stack."""
        # TODO: Set self.top = None (no nodes yet)
        # TODO: Set self._size = 0
        self.top = None
        self._size = 0
        

    def push(self, item):
        """
        Push an item onto the top of the stack.

        This is a linked list PREPEND:
        1. Create a new node
        2. Point new node's .next to current top
        3. Update top to the new node
        4. Increment size

        Args:
            item: The value to push

        Example:
            s.push(10)  # top -> [10 | None]
            s.push(20)  # top -> [20 | ---]--> [10 | None]
            s.push(30)  # top -> [30 | ---]--> [20 | ---]--> [10 | None]
        """
        # TODO: Create a new Node with the item
        # TODO: Point new_node.next to self.top
        # TODO: Update self.top to new_node
        # TODO: Increment self._size
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1


    def pop(self):
        """
        Remove and return the top item from the stack.

        This is a linked list HEAD REMOVAL:
        1. Save the top node's data
        2. Update top to top.next
        3. Decrement size
        4. Return the saved data

        Raises:
            IndexError: If the stack is empty

        Returns:
            The value that was on top

        Example:
            s = [30 -> 20 -> 10]
            s.pop()  # Returns 30, stack becomes [20 -> 10]
        """
        # TODO: If empty, raise IndexError("Stack is empty")
        # TODO: Save self.top.data
        # TODO: Update self.top = self.top.next
        # TODO: Decrement self._size
        # TODO: Return the saved data
        if self.is_empty():
            raise IndexError("Stack is empty.")
        data = self.top.data
        self.top = self.top.next
        self._size -=1
        return data

    def peek(self):
        """
        Return the top item WITHOUT removing it.

        Raises:
            IndexError: If the stack is empty

        Returns:
            The value on top

        Example:
            s = [30 -> 20 -> 10]
            s.peek()  # Returns 30, stack unchanged
        """
        # TODO: If empty, raise IndexError("Stack is empty")
        # TODO: Return self.top.data
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        """
        Check if the stack has no items.

        Returns:
            True if empty, False otherwise
        """
        # TODO: Return whether self.top is None
        return self.top is None

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            Integer count of items
        """
        # TODO: Return self._size
        return self._size


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 10 - QUESTION 1: STACK USING A LINKED LIST")
    print("=" * 60)

    # Test 1: Basic push and peek
    print("\nTEST 1: Basic push and peek")
    print("-" * 40)
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    result = s.peek()
    status = "PASS" if result == 30 else "FAIL"
    print(f"  Push 10, 20, 30:")
    print(f"  peek() -> {result} (Expected: 30) {status}")

    result = s.size()
    status = "PASS" if result == 3 else "FAIL"
    print(f"  size() -> {result} (Expected: 3) {status}")
    print()

    # Test 2: Pop elements
    print("TEST 2: Pop elements")
    print("-" * 40)
    result = s.pop()
    status = "PASS" if result == 30 else "FAIL"
    print(f"  pop() -> {result} (Expected: 30) {status}")

    result = s.pop()
    status = "PASS" if result == 20 else "FAIL"
    print(f"  pop() -> {result} (Expected: 20) {status}")

    result = s.peek()
    status = "PASS" if result == 10 else "FAIL"
    print(f"  peek() -> {result} (Expected: 10) {status}")

    result = s.size()
    status = "PASS" if result == 1 else "FAIL"
    print(f"  size() -> {result} (Expected: 1) {status}")
    print()

    # Test 3: Empty stack behavior
    print("TEST 3: Empty stack behavior")
    print("-" * 40)
    s2 = Stack()

    result = s2.is_empty()
    status = "PASS" if result == True else "FAIL"
    print(f"  New stack is_empty() -> {result} (Expected: True) {status}")

    try:
        s2.pop()
        print(f"  Pop from empty -> NO ERROR (Expected: IndexError) FAIL")
    except IndexError:
        print(f"  Pop from empty -> IndexError raised (Expected: IndexError) PASS")

    try:
        s2.peek()
        print(f"  Peek from empty -> NO ERROR (Expected: IndexError) FAIL")
    except IndexError:
        print(f"  Peek from empty -> IndexError raised (Expected: IndexError) PASS")
    print()

    # Test 4: Push after pop (reuse)
    print("TEST 4: Push after pop (reuse)")
    print("-" * 40)
    s3 = Stack()
    s3.push(1)
    s3.push(2)
    s3.pop()
    s3.pop()

    result = s3.is_empty()
    status = "PASS" if result == True else "FAIL"
    print(f"  Push 1, 2, pop, pop -> is_empty() = {result} (Expected: True) {status}")

    s3.push(99)
    result = s3.peek()
    status = "PASS" if result == 99 else "FAIL"
    print(f"  Push 99 -> peek() = {result} (Expected: 99) {status}")

    result = s3.size()
    status = "PASS" if result == 1 else "FAIL"
    print(f"  size() = {result} (Expected: 1) {status}")
    print()

    # Test 5: Verify no Python list used
    print("TEST 5: Verify linked list implementation")
    print("-" * 40)
    s4 = Stack()
    s4.push(10)
    has_top = hasattr(s4, 'top')
    has_items = hasattr(s4, 'items')
    status = "PASS" if has_top and not has_items else "FAIL"
    print(f"  Has 'top' attribute: {has_top}")
    print(f"  Has 'items' attribute (Python list): {has_items}")
    print(f"  Uses linked list, not Python list: {status}")

    if has_top and s4.top is not None:
        is_node = isinstance(s4.top, Node)
        status = "PASS" if is_node else "FAIL"
        print(f"  top is a Node object: {is_node} {status}")
    print()

    # Bonus
    print("=" * 60)
    print("BONUS CHALLENGES:")
    print("-" * 60)
    print("  1. Add a display() method that shows the stack top-to-bottom")
    print("  2. Add a __str__ method so you can print(stack)")
    print("  3. Implement __len__ so you can use len(stack)")
    print("  4. Compare performance: time 100,000 push/pops vs Python list stack")


if __name__ == "__main__":
    run_tests()
