# Subarrays with Given Sum and Bounded Maximum

## 💡 Intuition & Approach
We find subarrays summing to $k$ with elements $\le M$ in a single pass by treating elements $> M$ as absolute **walls**. 

When a wall is hit, the previous history becomes meaningless because no valid subarray can cross it. We dynamically segment the array by resetting `running_sum = 0` and clearing our map back to `{0: 1}`. For valid elements, we use the **Prefix Sum + Hash Map** pattern to count matches in $O(1)$ time.

### 📐 The Vector Intuition
Think of finding a valid range $AB$, where $O$ is the absolute starting root of the current segment:

$$OA + AB = OB \implies AB = OB - OA$$

* **$OB$** is the cumulative sum from the segment root up to the current index $B$ (`running_sum`).
* **$AB$** is the targeted target sum ($k$).
* **$OA$** is the historical prefix sum we need to look up in our hash map (`running_sum - k`).

### ❓ Why initialize with `{0: 1}`?
Allows `running_sum - k = 0` to successfully catch a single element that equals $k$, or any valid subarray that starts from the absolute beginning of the segment.

## 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | The array is processed in a single linear pass. Dictionary lookups and insertions operate in $O(1)$ average time. |
| **Space** | $O(n)$ | In the worst-case scenario (no elements exceed $M$), the hash map stores up to $n$ unique prefix sum frequencies. |

## 🛠️ Technical Details
- **Pattern:** Prefix Sum / Hash Map Lookup (Two-Sum Variation)
- **Edge Cases Handled:**
    - **Zero Elements:** Handled gracefully by immediate loop termination on empty inputs.
    - **Single Element:** Validated accurately against both $k$ and $M$ thresholds.
    - **Zero Extensions:** Correctly tracks multiple sub-segments when `0` pads or extends an existing valid sum.
    - **Negative Numbers:** The prefix sum handles fluctuating values smoothly within valid segments without breaking window bounds.

## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.