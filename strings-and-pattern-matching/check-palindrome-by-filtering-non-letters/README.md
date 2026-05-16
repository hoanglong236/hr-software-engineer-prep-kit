# Check Palindrome by Filtering Non-Letters

## 💡 Intuition & Approach
We use a **Two-Pointer technique** to validate the palindrome in-place without wasting memory on a filtered copy of the string. 

Pointers `l` (left) and `r` (right) move inward from the string boundaries. Inner loops skip non-alphabetic characters. When both pointers land on letters, we compare them case-insensitively. Any mismatch returns `False` immediately; if pointers cross without a mismatch, we return `True`.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | Each character in the string is visited exactly once during the linear scan. |
| **Space** | $O(1)$ | Constant memory used exclusively for the two index pointers. |

## 🛠️ Technical Details
- **Pattern:** Two Pointers (Opposite Direction)
- **Edge Cases Handled:**
    - **Empty String / Single Letter:** Safely bypasses evaluation loop and returns `True`.
    - **Pure Non-Letters (`"!@#"`):** Pointers converge cleanly at the center without index out-of-bounds errors, returning `True`.
    - **Mixed Casing:** Lowercases characters dynamically during comparisons to ignore case.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.