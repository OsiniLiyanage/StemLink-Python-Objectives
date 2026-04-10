"""
SESSION 11 - QUESTION 2: Hash Table from Scratch
=================================================
Topics: Hash functions, chaining, put/get/delete/contains

Instructions:
1. Implement all methods in the HashTable class
2. Use chaining (lists of [key, value] pairs) for collision handling
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


class HashTable:
    """A hash table using chaining for collision resolution.

    Internal structure:
        self.size = number of slots
        self.table = list of lists (chains)
        Example with size=5:
            [
                [],                         # slot 0
                [["alice", 85]],            # slot 1
                [],                         # slot 2
                [["bob", 90], ["eve", 78]], # slot 3 (collision!)
                [],                         # slot 4
            ]
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Compute the hash index for a given key.

        Returns: hash(key) % self.size
        """
        # TODO: Return hash(key) % self.size
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair.

        If the key already exists, UPDATE its value (don't create a duplicate).
        If the key is new, append [key, value] to the chain.

        Hint:
            1. Compute the index using self._hash(key)
            2. Get the chain at that index
            3. Loop through the chain to check if key already exists
            4. If found, update the value
            5. If not found, append [key, value]
        """
        # TODO: Implement put with update-or-insert logic
        index = self._hash(key)
        chain = self.table[index]
        for pair in chain:
            if pair[0] == key:
                pair[1] = value
                return
        chain.append([key,value])

    def get(self, key):
        """Retrieve the value for a given key.

        Returns: The value associated with the key
        Raises: KeyError if the key is not found
        """
        # TODO: Compute index, search the chain, return value or raise KeyError
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] ==key:
                return pair[1]
        raise KeyError(key)

    def delete(self, key):
        """Remove a key-value pair from the hash table.

        Raises: KeyError if the key is not found

        Hint: Loop through the chain with enumerate() to get the index
              for removal, then use chain.pop(i)
        """
        # TODO: Compute index, find the pair in the chain, remove it
        index = self._hash(key)
        chain = self.table[index]
        for i, pair in enumerate(chain):
            if pair[0] == key:
                chain.pop(i)
                return
        raise KeyError(key)

    def contains(self, key):
        """Return True if the key exists in the hash table."""
        # TODO: Try to get the key; return True if found, False if KeyError
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        """Return a list of all keys in the hash table."""
        all_keys = []
        for chain in self.table:
            for pair in chain:
                all_keys.append(pair[0])
        return all_keys

    def __str__(self):
        items = []
        for chain in self.table:
            for pair in chain:
                items.append(f"{pair[0]}: {pair[1]}")
        return "HashTable({" + ", ".join(items) + "})"


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 11 - QUESTION 2: HASH TABLE")
    print("=" * 60)

    # Test 1: Put and get
    print("\nTEST 1: Put and get")
    print("-" * 40)
    ht = HashTable(size=5)
    ht.put("alice", 85)
    ht.put("bob", 90)
    ht.put("charlie", 78)

    result = ht.get("alice")
    status = "PASS" if result == 85 else "FAIL"
    print(f"  put('alice', 85), get('alice') -> {result} (Expected: 85) {status}")

    result = ht.get("bob")
    status = "PASS" if result == 90 else "FAIL"
    print(f"  put('bob', 90), get('bob') -> {result} (Expected: 90) {status}")

    # Test 2: Update existing key
    print("\nTEST 2: Update existing key")
    print("-" * 40)
    ht.put("alice", 95)
    result = ht.get("alice")
    status = "PASS" if result == 95 else "FAIL"
    print(f"  put('alice', 95), get('alice') -> {result} (Expected: 95) {status}")

    # Verify no duplicate - count occurrences of 'alice' in chains
    alice_count = sum(1 for chain in ht.table for pair in chain if pair[0] == "alice")
    status = "PASS" if alice_count == 1 else "FAIL"
    print(f"  'alice' appears {alice_count} time(s) in table (Expected: 1) {status}")

    # Test 3: Contains
    print("\nTEST 3: Contains")
    print("-" * 40)
    result = ht.contains("bob")
    status = "PASS" if result == True else "FAIL"
    print(f"  contains('bob') -> {result} (Expected: True) {status}")

    result = ht.contains("dave")
    status = "PASS" if result == False else "FAIL"
    print(f"  contains('dave') -> {result} (Expected: False) {status}")

    # Test 4: Delete
    print("\nTEST 4: Delete")
    print("-" * 40)
    ht.delete("bob")
    result = ht.contains("bob")
    status = "PASS" if result == False else "FAIL"
    print(f"  delete('bob'), contains('bob') -> {result} (Expected: False) {status}")

    # Test 5: KeyError on get
    print("\nTEST 5: Error handling")
    print("-" * 40)
    try:
        ht.get("bob")
        print(f"  get('bob') after delete -> No error (Expected: KeyError) FAIL")
    except KeyError:
        print(f"  get('bob') after delete -> KeyError (Expected: KeyError) PASS")

    try:
        ht.delete("zzz")
        print(f"  delete('zzz') -> No error (Expected: KeyError) FAIL")
    except KeyError:
        print(f"  delete('zzz') -> KeyError (Expected: KeyError) PASS")

    # Test 6: Collisions (small table forces collisions)
    print("\nTEST 6: Collision handling (size=3)")
    print("-" * 40)
    small_ht = HashTable(size=3)
    words = ["cat", "dog", "rat", "bat", "ant"]
    for word in words:
        small_ht.put(word, len(word))

    all_found = True
    for word in words:
        try:
            val = small_ht.get(word)
            if val != len(word):
                all_found = False
        except KeyError:
            all_found = False
    status = "PASS" if all_found else "FAIL"
    print(f"  Inserted 5 words into size-3 table")
    print(f"  All 5 words retrievable: {all_found} (Expected: True) {status}")

    # Show table structure
    print(f"\n  Table structure:")
    for i, chain in enumerate(small_ht.table):
        print(f"    Slot {i}: {chain}")


if __name__ == "__main__":
    run_tests()
