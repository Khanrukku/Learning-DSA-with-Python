"""
Unit tests for array data structures and algorithms

Author: Rukaiya Khan
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.arrays import DynamicArray, binary_search, two_sum


def test_dynamic_array_initialization():
    """Test array initialization"""
    arr = DynamicArray()
    assert len(arr) == 0
    assert arr._capacity == 10


def test_dynamic_array_append():
    """Test append operation"""
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    
    assert len(arr) == 3
    assert arr[0] == 1
    assert arr[2] == 3


def test_dynamic_array_resize():
    """Test automatic resizing"""
    arr = DynamicArray(capacity=2)
    arr.append(1)
    arr.append(2)
    arr.append(3)  # Should trigger resize
    
    assert len(arr) == 3
    assert arr._capacity == 4


def test_binary_search():
    """Test binary search algorithm"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 10) == -1


def test_two_sum():
    """Test two sum algorithm"""
    arr = [2, 7, 11, 15]
    result = two_sum(arr, 9)
    
    assert result == [0, 1]
    
    result = two_sum(arr, 26)
    assert result == [2, 3]
    
    result = two_sum(arr, 100)
    assert result is None


if __name__ == "__main__":
    print("Running Array Tests...")
    test_dynamic_array_initialization()
    test_dynamic_array_append()
    test_dynamic_array_resize()
    test_binary_search()
    test_two_sum()
    print("✅ All tests passed!")
```

**Where**: `tests/test_arrays.py`

---

### **File 5: `.gitignore`**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Logs
*.log
