"""
SESSION 11 - QUESTION 1: Queue with collections.deque
=====================================================
Topics: FIFO ordering, collections.deque, Hot Potato simulation

Instructions:
1. Implement the Queue class using collections.deque
2. Implement the hot_potato() function
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""

from collections import deque


class Queue:
    """A queue (FIFO) implemented using collections.deque."""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        # TODO: Use deque's append method
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        # TODO: Use deque's popleft method
        # Hint: raise IndexError("Queue is empty") if nothing to dequeue
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self):
        """Return the front item without removing it.
        Raises IndexError if the queue is empty.
        """
        # TODO: Return self.items[0] if not empty
        # Hint: raise IndexError("Queue is empty") if nothing to peek
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        # TODO: Check if the deque has no items
        return len(self.items) ==0

    def size(self):
        """Return the number of items in the queue."""
        # TODO: Return the length of the deque
        return len(self.items)

    def __str__(self):
        return "Queue: " + str(list(self.items))


def hot_potato(names, k):
    """Simulate the Hot Potato game.

    Rules:
    - Players stand in a circle (use a queue to simulate this)
    - Pass the potato: dequeue from front, enqueue to back
    - Every k-th pass, the person holding the potato is eliminated
    - Last person remaining is the survivor

    Args:
        names: List of player names
        k: Number of passes before elimination

    Returns:
        The name of the surviving player

    Example:
        hot_potato(["Alice", "Bob", "Charlie", "David", "Eve"], 3)
        Pass 1: Alice goes to back -> [Bob, Charlie, David, Eve, Alice]
        Pass 2: Bob goes to back -> [Charlie, David, Eve, Alice, Bob]
        Pass 3: Charlie is ELIMINATED -> [David, Eve, Alice, Bob]
        ... continue until 1 player remains
    """
    # TODO: Create a queue and enqueue all players
    # TODO: While more than 1 player remains:
    #   - Pass the potato (k-1) times: dequeue from front, enqueue to back
    #   - On the k-th pass: dequeue and eliminate (don't re-enqueue)
    # TODO: Return the last remaining player

    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size()>1:
        for _ in range(k-1):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 11 - QUESTION 1: QUEUE")
    print("=" * 60)

    # Test 1: Basic queue operations
    print("\nTEST 1: Basic queue operations")
    print("-" * 40)
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"  Enqueue A, B, C:")

    result = q.front()
    status = "PASS" if result == "A" else "FAIL"
    print(f"  front() -> {result} (Expected: A) {status}")

    result = q.dequeue()
    status = "PASS" if result == "A" else "FAIL"
    print(f"  dequeue() -> {result} (Expected: A) {status}")

    result = q.size()
    status = "PASS" if result == 2 else "FAIL"
    print(f"  size() -> {result} (Expected: 2) {status}")

    result = q.front()
    status = "PASS" if result == "B" else "FAIL"
    print(f"  front() -> {result} (Expected: B) {status}")

    # Test 2: Empty queue check
    print("\nTEST 2: Empty queue operations")
    print("-" * 40)
    q2 = Queue()
    result = q2.is_empty()
    status = "PASS" if result == True else "FAIL"
    print(f"  New queue is_empty() -> {result} (Expected: True) {status}")

    q2.enqueue("X")
    result = q2.is_empty()
    status = "PASS" if result == False else "FAIL"
    print(f"  After enqueue, is_empty() -> {result} (Expected: False) {status}")

    q2.dequeue()
    result = q2.is_empty()
    status = "PASS" if result == True else "FAIL"
    print(f"  After dequeue, is_empty() -> {result} (Expected: True) {status}")

    # Test 3: Error handling
    print("\nTEST 3: Error handling")
    print("-" * 40)
    q3 = Queue()
    try:
        q3.dequeue()
        print(f"  dequeue() on empty -> No error (Expected: IndexError) FAIL")
    except IndexError:
        print(f"  dequeue() on empty -> IndexError (Expected: IndexError) PASS")

    try:
        q3.front()
        print(f"  front() on empty -> No error (Expected: IndexError) FAIL")
    except IndexError:
        print(f"  front() on empty -> IndexError (Expected: IndexError) PASS")

    # Test 4: FIFO ordering
    print("\nTEST 4: FIFO ordering")
    print("-" * 40)
    q4 = Queue()
    for i in range(1, 6):
        q4.enqueue(i)
    order = []
    while not q4.is_empty():
        order.append(q4.dequeue())
    status = "PASS" if order == [1, 2, 3, 4, 5] else "FAIL"
    print(f"  Enqueue 1-5, dequeue all -> {order}")
    print(f"  Expected: [1, 2, 3, 4, 5] {status}")

    # Test 5: Hot Potato
    print("\nTEST 5: Hot Potato game")
    print("-" * 40)
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    result = hot_potato(names, 3)
    status = "PASS" if result == "David" else "FAIL"
    print(f"  Players: {names}, k=3")
    print(f"  Survivor: {result} (Expected: David) {status}")

    names2 = ["A", "B", "C", "D", "E", "F"]
    result2 = hot_potato(names2, 2)
    status2 = "PASS" if result2 == "E" else "FAIL"
    print(f"  Players: {names2}, k=2")
    print(f"  Survivor: {result2} (Expected: E) {status2}")


if __name__ == "__main__":
    run_tests()
