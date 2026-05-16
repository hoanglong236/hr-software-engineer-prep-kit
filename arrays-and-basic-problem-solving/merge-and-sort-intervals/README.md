# Merge and Sort Intervals

## 💡 Intuition & Approach
We sort the intervals by their start times to establish a predictable timeline. We then iterate through the sorted list, comparing each interval with the last merged interval in our results list. Because the input is sorted, we only need to check if the current interval's start time is less than or equal to the last merged interval's end time. If it is, they overlap, and we merge them by extending the end boundary. Otherwise, they are disjoint, and we append the current interval as a new entry.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n \log n)$ | Sorting the intervals dominates the time complexity. The subsequent linear scan takes $O(n)$ time. |
| **Space** | $O(n)$ | Allocating space for the output array. In the worst-case scenario, no intervals overlap. |

## 🛠️ Technical Details
- **Pattern:** Sorting / Linear Scan
- **Edge Cases Handled:**
    - **Adjacent Boundaries:** Intervals that touch at a single point (e.g., `[1, 2]` and `[2, 3]`) are successfully merged.
    - **Full Containment:** Smaller intervals completely swallowed by a larger preceding interval are ignored.
    - **Unordered Inputs:** Handles unsorted ranges safely due to the initial sort step.
    - **Duplicates & Empty Sets:** Edge cases with identical coordinates or zero elements are handled gracefully by guard clauses.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.