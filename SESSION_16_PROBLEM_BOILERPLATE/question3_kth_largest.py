"""
SESSION 16 - QUESTION 3: kth Largest Element
============================================
Topics: Sorting, heaps

Instructions:
1. Implement both versions of kth_largest
2. kth_largest_sort is O(n log n)
3. kth_largest_heap is O(n log k) using a min-heap of size k
4. Run this file to test your implementation
5. Do NOT modify the test code below the line
"""

import heapq


def kth_largest_sort(nums, k):
    """Return the k-th largest element using sorting. O(n log n).

    k = 1 is the largest, k = 2 is the second largest, etc.

    Args:
        nums: List of integers (unsorted)
        k:    Positive integer (1 <= k <= len(nums))

    Returns:
        The k-th largest element

    Examples:
        kth_largest_sort([3, 2, 1, 5, 6, 4], 2)             -> 5
        kth_largest_sort([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)    -> 4

    Hint:
        nums_sorted = sorted(nums)
        return nums_sorted[-k]   # k-th from the end
    """
    # TODO: Implement kth_largest_sort
    
    nums.sort()
    return nums[-k]


def kth_largest_heap(nums, k):
    """Return the k-th largest element using a min-heap. O(n log k).

    Maintain a min-heap of size k of the largest values seen so far.
    The smallest element in this heap is the k-th largest overall.

    Args:
        nums: List of integers (unsorted)
        k:    Positive integer

    Returns:
        The k-th largest element

    Hint:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)     # discard the smallest
        return heap[0]                  # smallest in the size-k heap
    """
    # TODO: Implement kth_largest_heap
    
    h =[]
    for i in range(k):
        heapq.heappush(h,nums[i])
    for i in range(k,len(nums)):
        if nums[i] > h[0]:
            heapq.heappush(h,nums[i])
            heapq.heappop(h)
    return h[0]



# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 16 - QUESTION 3: KTH LARGEST ELEMENT")
    print("=" * 60)

    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 7, 7], 2, 7),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([-1, -2, -3, -4], 2, -2),
    ]
    for i, (nums, k, expected) in enumerate(cases, 1):
        print(f"\nTEST {i}: kth_largest_sort({nums}, {k})")
        print("-" * 40)
        result = kth_largest_sort(list(nums), k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    for i, (nums, k, expected) in enumerate(cases, len(cases) + 1):
        print(f"\nTEST {i}: kth_largest_heap({nums}, {k})")
        print("-" * 40)
        result = kth_largest_heap(list(nums), k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
