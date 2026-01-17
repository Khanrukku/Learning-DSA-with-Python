"""
Arrays and Dynamic Arrays Implementation
==========================================

Time Complexity Analysis:
- Access: O(1)
- Search: O(n)
- Insert (end): O(1) amortized, O(n) worst case
- Insert (arbitrary): O(n)
- Delete: O(n)

Space Complexity: O(n)

Author: Rukaiya Khan
Research Focus: Fundamental data structure implementation and analysis
"""

class DynamicArray:
    """
    Dynamic array implementation with automatic resizing.
    
    Key Features:
    - Automatic capacity doubling when full
    - Amortized O(1) append operation
    - Memory-efficient shrinking
    
    Research Notes:
    - Resizing strategy: Double capacity when full, halve when 1/4 full
    - This provides amortized O(1) insertions while avoiding thrashing
    """
    
    def __init__(self, capacity=10):
        """Initialize dynamic array with given capacity"""
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity
    
    def __len__(self):
        """Return number of elements"""
        return self._size
    
    def __getitem__(self, index):
        """
        Get element at index.
        Time Complexity: O(1)
        """
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def __setitem__(self, index, value):
        """
        Set element at index.
        Time Complexity: O(1)
        """
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value
    
    def append(self, value):
        """
        Add element to end of array.
        
        Time Complexity: 
        - Average: O(1) amortized
        - Worst: O(n) when resizing needed
        
        Amortized Analysis:
        - n insertions: n + n/2 + n/4 + ... = 2n operations
        - Average per insertion: 2n/n = O(1)
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        self._array[self._size] = value
        self._size += 1
    
    def insert(self, index, value):
        """
        Insert element at specific index.
        
        Time Complexity: O(n)
        - Must shift all elements after index
        """
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds")
        
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        
        # Shift elements right
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        
        self._array[index] = value
        self._size += 1
    
    def remove(self, value):
        """
        Remove first occurrence of value.
        
        Time Complexity: O(n)
        - O(n) search + O(n) shift = O(n)
        """
        for i in range(self._size):
            if self._array[i] == value:
                self.pop(i)
                return
        raise ValueError(f"{value} not found in array")
    
    def pop(self, index=-1):
        """
        Remove and return element at index.
        
        Time Complexity: O(n)
        - O(1) if index is last element
        - O(n) otherwise due to shifting
        """
        if self._size == 0:
            raise IndexError("Pop from empty array")
        
        if index < 0:
            index = self._size + index
        
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        
        value = self._array[index]
        
        # Shift elements left
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        
        self._array[self._size - 1] = None
        self._size -= 1
        
        # Shrink if needed (avoid thrashing)
        if self._size > 0 and self._size == self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return value
    
    def _resize(self, new_capacity):
        """
        Resize internal array to new capacity.
        
        Time Complexity: O(n)
        - Must copy all elements to new array
        
        Research Note:
        - This operation is expensive but infrequent
        - Amortized analysis shows average O(1) per insertion
        """
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
    
    def __str__(self):
        """String representation"""
        return '[' + ', '.join(str(self._array[i]) for i in range(self._size)) + ']'


def binary_search(arr, target):
    """
    Binary search on sorted array.
    
    Time Complexity: O(log n)
    Space Complexity: O(1) - iterative version
    
    Algorithm:
    1. Compare target with middle element
    2. If equal, found!
    3. If target < middle, search left half
    4. If target > middle, search right half
    5. Repeat until found or search space empty
    
    Recurrence Relation: T(n) = T(n/2) + O(1) = O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found


def two_sum(arr, target):
    """
    Find two numbers that sum to target.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Algorithm: Hash table approach
    - Store complements in hash table as we iterate
    - For each element, check if complement exists
    
    Research Note:
    - Classic time-space tradeoff
    - Sorting + two pointers: O(n log n) time, O(1) space
    - Hash table: O(n) time, O(n) space
    """
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None


# Example usage and testing
if __name__ == "__main__":
    print("Dynamic Array Implementation Demo")
    print("=" * 50)
    
    # Create dynamic array
    arr = DynamicArray()
    
    # Test append
    print("\n1. Testing append operation:")
    for i in range(15):
        arr.append(i)
    print(f"Array after 15 appends: {arr}")
    print(f"Length: {len(arr)}, Capacity: {arr._capacity}")
    
    # Test insert
    print("\n2. Testing insert operation:")
    arr.insert(5, 99)
    print(f"After insert(5, 99): {arr}")
    
    # Test remove
    print("\n3. Testing remove operation:")
    arr.remove(99)
    print(f"After remove(99): {arr}")
    
    # Test pop
    print("\n4. Testing pop operation:")
    popped = arr.pop()
    print(f"Popped value: {popped}")
    print(f"Array after pop: {arr}")
    
    # Test binary search
    print("\n5. Testing binary search:")
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    result = binary_search(sorted_arr, target)
    print(f"Searching for {target} in {sorted_arr}")
    print(f"Found at index: {result}")
    
    # Test two sum
    print("\n6. Testing two sum problem:")
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Indices: {result}")
