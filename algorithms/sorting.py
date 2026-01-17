"""
Sorting Algorithms Implementation and Analysis
==============================================

Comprehensive implementation of classical sorting algorithms
with complexity analysis and performance benchmarking.

Author: Rukaiya Khan
Research Focus: Comparative analysis of sorting algorithms

Time Complexity Summary:
-------------------------
Algorithm       | Best      | Average   | Worst     | Space | Stable
----------------|-----------|-----------|-----------|-------|-------
Bubble Sort     | O(n)      | O(n²)     | O(n²)     | O(1)  | Yes
Selection Sort  | O(n²)     | O(n²)     | O(n²)     | O(1)  | No
Insertion Sort  | O(n)      | O(n²)     | O(n²)     | O(1)  | Yes
Merge Sort      | O(n log n)| O(n log n)| O(n log n)| O(n)  | Yes
Quick Sort      | O(n log n)| O(n log n)| O(n²)     | O(log n)| No
Heap Sort       | O(n log n)| O(n log n)| O(n log n)| O(1)  | No
"""

def bubble_sort(arr):
    """
    Bubble Sort - Simple comparison-based sorting
    
    Time Complexity:
    - Best: O(n) - already sorted, with optimization
    - Average: O(n²)
    - Worst: O(n²)
    
    Space Complexity: O(1) - in-place
    
    Algorithm:
    - Repeatedly swap adjacent elements if they're in wrong order
    - After each pass, largest element "bubbles" to end
    - Optimization: Stop if no swaps in a pass
    
    When to use:
    - Small datasets (n < 50)
    - Nearly sorted data
    - Educational purposes
    
    When to avoid:
    - Large datasets
    - Performance-critical applications
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimization: if no swaps, array is sorted
        if not swapped:
            break
    
    return arr


def insertion_sort(arr):
    """
    Insertion Sort - Building sorted array one element at a time
    
    Time Complexity:
    - Best: O(n) - already sorted
    - Average: O(n²)
    - Worst: O(n²) - reverse sorted
    
    Space Complexity: O(1) - in-place
    
    Algorithm:
    - Divide array into sorted and unsorted portions
    - Pick element from unsorted, insert into correct position in sorted
    - Like sorting playing cards in your hand
    
    Advantages:
    - Simple implementation
    - Efficient for small data (n < 50)
    - Efficient for nearly sorted data
    - Stable sort
    - Online algorithm (can sort as data arrives)
    
    Research Note:
    - Used in practice for small subarrays in hybrid algorithms
    - Timsort uses insertion sort for small runs
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than key to right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr):
    """
    Merge Sort - Divide and conquer sorting
    
    Time Complexity: O(n log n) - all cases
    Space Complexity: O(n) - requires auxiliary array
    
    Algorithm:
    1. Divide array into two halves
    2. Recursively sort each half
    3. Merge sorted halves
    
    Recurrence: T(n) = 2T(n/2) + O(n) = O(n log n)
    
    Advantages:
    - Guaranteed O(n log n) performance
    - Stable sort
    - Predictable performance
    - Good for linked lists
    
    Disadvantages:
    - Requires O(n) extra space
    - Not in-place
    - Slower than quicksort in practice for arrays
    
    When to use:
    - Need guaranteed O(n log n)
    - Stability required
    - Sorting linked lists
    - External sorting
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)


def merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort - Efficient divide and conquer
    
    Time Complexity:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n²) - rare with good pivot selection
    
    Space Complexity: O(log n) - recursion stack
    
    Algorithm:
    1. Choose pivot element
    2. Partition: elements < pivot go left, > pivot go right
    3. Recursively sort partitions
    
    Pivot Selection Strategies:
    - First element: Simple but worst case on sorted data
    - Last element: Same issue
    - Random: Good average case
    - Median-of-three: Best in practice
    
    Advantages:
    - Fast in practice (cache-friendly)
    - In-place (low space overhead)
    - Average O(n log n)
    
    Research Note:
    - Most used sorting algorithm in practice
    - Hybrid approaches (introsort) switch to heapsort if recursion deep
    """
    if len(arr) <= 1:
        return arr
    
    # Median-of-three pivot selection
    pivot = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# Example usage and benchmarking
if __name__ == "__main__":
    import random
    import time
    
    print("Sorting Algorithms Comparison")
    print("=" * 60)
    
    # Test data
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        print(f"\nArray size: {size}")
        print("-" * 60)
        
        # Generate random array
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
        ]
        
        for name, func in algorithms:
            start = time.time()
            sorted_arr = func(arr)
            end = time.time()
            
            # Verify correctness
            is_sorted = sorted_arr == sorted(arr)
            
            print(f"{name:20s}: {(end-start)*1000:8.2f}ms | Correct: {is_sorted}")
        
    # Demonstrate best/worst cases
    print("\n\nBest/Worst Case Analysis")
    print("=" * 60)
    
    print("\nBest Case (Already Sorted):")
    sorted_arr = list(range(1000))
    
    start = time.time()
    bubble_sort(sorted_arr)
    print(f"Bubble Sort: {(time.time()-start)*1000:.2f}ms")
    
    start = time.time()
    insertion_sort(sorted_arr)
    print(f"Insertion Sort: {(time.time()-start)*1000:.2f}ms")
    
    print("\nWorst Case (Reverse Sorted):")
    reverse_arr = list(range(1000, 0, -1))
    
    start = time.time()
    bubble_sort(reverse_arr)
    print(f"Bubble Sort: {(time.time()-start)*1000:.2f}ms")
    
    start = time.time()
    insertion_sort(reverse_arr)
    print(f"Insertion Sort: {(time.time()-start)*1000:.2f}ms")
