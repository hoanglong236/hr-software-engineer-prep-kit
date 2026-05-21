# 🎯 Two Sum (Task Pair Allocation)

## 💡 Intuition & Approach
We scan the array in a **single linear pass** using a hash map to track previously seen values and their respective indices. 

For each task duration `v`, we check if its complement (`slotLength - v`) already exists in the tracking map. If found, we instantly return the historical index alongside the current index `i`. Storing the current element *after* performing the lookup guarantees that an element can never falsely match with itself, eliminating the need for nested index validation.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | The array is processed in a single linear pass with $O(1)$ average hash map lookup time. |
| **Space** | $O(n)$ | In the worst-case scenario where no valid pair exists, the map scales proportionally to store all elements. |

## 🛠️ Technical Details
- **Pattern:** Hashing / Complement Index Mapping
- **Edge Cases Handled:**
    - **Empty Array / Single Element:** Returns `[-1, -1]` immediately since a valid pair requires two distinct tasks.
    - **No Valid Pair Available:** Safely runs through the entire array and defaults to returning `[-1, -1]` if no complement match hits.
    - **Self-Collision Prevention (`test_prevents_matching_element_with_itself`):** Solved natively by checking the map before inserting the active index.
    - **Duplicate Values:** Correctly handles multiple identical entries without overwriting or skipping potential target balances.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.