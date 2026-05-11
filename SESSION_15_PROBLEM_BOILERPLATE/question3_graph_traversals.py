"""
SESSION 15 - QUESTION 3: Graph Traversals
=========================================
Topics: BFS and DFS on an adjacency-list graph

Instructions:
1. Implement bfs and dfs
2. Both must use a visited set to avoid infinite loops on cycles
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""

from collections import deque


def bfs(graph, start):
    """Breadth-first search from `start`. Return nodes in BFS order.

    Within each iteration, visit neighbors in the order they appear in
    graph[node].

    Args:
        graph: Adjacency list (dict mapping node -> list of neighbors)
        start: The starting node

    Returns:
        A list of nodes in BFS order

    Examples:
        graph = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
        bfs(graph, 'A') -> ['A', 'B', 'C', 'D']

    Hint:
        1. visited = set([start])
        2. queue = deque([start])
        3. result = []
        4. While queue:
             node = queue.popleft()
             result.append(node)
             For neighbor in graph[node]:
               If neighbor not in visited:
                 visited.add(neighbor)
                 queue.append(neighbor)
        5. Return result
    """
    # TODO: Implement bfs
    visited = set([start])
    queue = deque([start])
    result =[]
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs(graph, start):
    """Depth-first search from `start`. Return nodes in DFS order.

    Use recursion. Within each call, visit neighbors in the order they
    appear in graph[node].

    Args:
        graph: Adjacency list (dict mapping node -> list of neighbors)
        start: The starting node

    Returns:
        A list of nodes in DFS order

    Examples:
        graph = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
        dfs(graph, 'A') -> ['A', 'B', 'D', 'C']

    Hint:
        Use a recursive helper that takes the current node and the
        visited set:

        def helper(node, visited):
            visited.add(node)
            result = [node]
            for neighbor in graph[node]:
                if neighbor not in visited:
                    result.extend(helper(neighbor, visited))
            return result

        return helper(start, set())
    """
    # TODO: Implement dfs (recursive)
    
    def helper(node,visited):
        visited.add(node)
        result =[node]
        for neighbor in graph[node]:
            if neighbor not in visited:
                result.extend(helper(neighbor,visited))
        return result
    return helper(start,set())



# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 15 - QUESTION 3: GRAPH TRAVERSALS")
    print("=" * 60)

    g1 = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
    g2 = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
    g3 = {'X': []}                # single node, no neighbors

    bfs_tests = [
        (g1, 'A', ['A', 'B', 'C', 'D']),
        (g2, 1, [1, 2, 3, 4]),
        (g3, 'X', ['X']),
    ]
    for i, (graph, start, expected) in enumerate(bfs_tests, 1):
        print(f"\nTEST {i}: bfs({graph}, {start!r})")
        print("-" * 40)
        result = bfs(graph, start)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")

    dfs_tests = [
        (g1, 'A', ['A', 'B', 'D', 'C']),
        (g2, 1, [1, 2, 4, 3]),
        (g3, 'X', ['X']),
    ]
    for i, (graph, start, expected) in enumerate(dfs_tests, len(bfs_tests) + 1):
        print(f"\nTEST {i}: dfs({graph}, {start!r})")
        print("-" * 40)
        result = dfs(graph, start)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
