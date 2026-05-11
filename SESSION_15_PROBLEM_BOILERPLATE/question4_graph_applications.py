"""
SESSION 15 - QUESTION 4: Graph Applications (BONUS)
===================================================
Topics: Connected components, shortest path on unweighted graphs

Instructions:
1. Implement both functions
2. count_components: BFS or DFS from each unvisited node
3. shortest_path: BFS, carrying the path along with each queue entry
4. Run this file to test your implementation
5. Do NOT modify the test code below the line
"""

from collections import deque


def count_components(graph):
    """Count the number of connected components in an undirected graph.

    A "component" is a group of nodes where every node can be reached
    from every other node via edges.

    Args:
        graph: Adjacency list (dict mapping node -> list of neighbors).
               The graph is undirected (if A->B is in the list, B->A is too).

    Returns:
        Integer count of connected components

    Examples:
        # Two components: {A,B} and {C}
        count_components({'A':['B'], 'B':['A'], 'C':[]})  -> 2

        # One big component
        count_components({'A':['B'], 'B':['A','C'], 'C':['B']})  -> 1

        # Each node is alone
        count_components({1: [], 2: [], 3: []})  -> 3

        # Empty graph
        count_components({})  -> 0

    Hint:
        1. visited = set()
        2. count = 0
        3. For each node in graph:
             If node not in visited:
               # New component! Run BFS or DFS to mark all reachable nodes.
               count += 1
               # Mark every node reachable from `node` as visited
               (use a queue or recursive DFS)
        4. Return count
    """
    # TODO: Implement count_components using BFS or DFS
    
    visited = set()
    count =0
    for node in graph:
        if node not in visited:
            count +=1
            queue = deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    return count


def shortest_path(graph, start, end):
    """Shortest path from `start` to `end` on an unweighted graph.
    Return the path as a list of nodes. Return None if no path exists.

    Args:
        graph: Adjacency list (dict mapping node -> list of neighbors)
        start: Starting node
        end:   Ending node

    Returns:
        A list of nodes from start to end (inclusive), or None

    Examples:
        graph = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
        shortest_path(graph, 'A', 'D')  -> ['A', 'B', 'D']
        shortest_path(graph, 'A', 'A')  -> ['A']

        graph2 = {'A':['B'], 'B':['A'], 'C':[]}
        shortest_path(graph2, 'A', 'C') -> None

    Hint:
        Use BFS where each queue entry is (node, path_so_far):
        1. queue = deque([(start, [start])])
        2. visited = {start}
        3. While queue:
             node, path = queue.popleft()
             If node == end: return path
             For neighbor in graph[node]:
               If neighbor not in visited:
                 visited.add(neighbor)
                 queue.append((neighbor, path + [neighbor]))
        4. Return None
    """
    # TODO: Implement shortest_path with BFS
    

    queue = deque([(start,[start])])
    visited ={start}
    while queue:
        node,path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path + [neighbor]))
    return None



# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 15 - QUESTION 4: GRAPH APPLICATIONS (BONUS)")
    print("=" * 60)

    cc_tests = [
        ({'A': ['B'], 'B': ['A'], 'C': []}, 2),
        ({'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}, 1),
        ({1: [], 2: [], 3: []}, 3),
        ({}, 0),
        ({'A': ['B'], 'B': ['A'], 'C': ['D'], 'D': ['C'], 'E': []}, 3),
    ]
    for i, (graph, expected) in enumerate(cc_tests, 1):
        print(f"\nTEST {i}: count_components({graph})")
        print("-" * 40)
        result = count_components(graph)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    g1 = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
    g2 = {'A': ['B'], 'B': ['A'], 'C': []}
    g3 = {1: [2, 3], 2: [1, 4], 3: [1, 5], 4: [2, 6], 5: [3, 6], 6: [4, 5]}

    sp_tests = [
        (g1, 'A', 'D', ['A', 'B', 'D']),
        (g1, 'A', 'A', ['A']),
        (g2, 'A', 'C', None),
        (g3, 1, 6, [1, 2, 4, 6]),
        (g3, 1, 1, [1]),
    ]
    for i, (graph, start, end, expected) in enumerate(sp_tests, len(cc_tests) + 1):
        print(f"\nTEST {i}: shortest_path(graph, {start!r}, {end!r})")
        print("-" * 40)
        result = shortest_path(graph, start, end)
        # Accept any path of the same length (multiple shortest paths can exist)
        if expected is None:
            status = "PASS" if result is None else "FAIL"
        elif result is None:
            status = "FAIL"
        else:
            status = "PASS" if (len(result) == len(expected)
                                and result[0] == start
                                and result[-1] == end) else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected} (or any path of the same length)")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
