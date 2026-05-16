# Count Elements Greater Than Previous Average

## 💡 Intuition & Approach 
> Instead of recalculating the average at every step (which would be $O(n^2)$), I implemented a **prefix sum** approach. This allows us to determine the average of all previous elements in constant time $O(1)$ during a single traversal.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | We iterate through the input array exactly once. |
| **Space** | $O(1)$ | We only store a few scalar variables (total, ans) regardless of input size. |

## 🛠️ Technical Details
- **Language:** Python 3.14
- **Pattern:** Prefix Sum (Running Total)
- **Edge Cases Handled:**
    - Empty input lists (returns 0).
    - Single element lists (index 0 has no preceding elements to average).
    - Values exactly equal to the average (validates "strictly greater" logic).

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.