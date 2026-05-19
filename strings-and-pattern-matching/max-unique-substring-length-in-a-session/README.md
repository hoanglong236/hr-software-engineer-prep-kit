# Max Unique Substring Length in a Session

## 🚀 Solution 0 (Optimal Single-Pass)

### 💡 Intuition & Approach
We scan the string linearly using a **Sliding Window**. Characters matching `*` act as hard **session walls**. 

When a wall is hit, we instantly reset tracking by clearing the hash map and shifting our starting boundary (`pivot`) past the wall. For valid characters, a hash map tracks their last seen index. If a duplicate appears within the active session, `pivot` safely jumps past its previous occurrence to maintain a window of unique characters.

### 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | The string is processed in a single linear pass with $O(1)$ map operations. |
| **Space** | $O(\min(n, \Sigma))$ | The map stores at most the total number of unique characters ($\Sigma$) within one session. |

### 🛠️ Technical Details
- **Pattern:** Sliding Window / Hash Map Index Tracking


## 🧱 Solution 1 (String Split + Relative Distance Mapping)

### 💡 Intuition & Approach
This solution uses `.split('*')` to isolate clean session segments, tracking each character's last seen index inside a fixed-size array of size 26.

Rely on relative-distance mathematics. If the distance between the current index `i` and the character's last seen index is strictly greater than `window_size`, the previous duplicate is mathematically guaranteed to sit outside the current active window. This allows `window_size` to safely expand without triggering a false collision.

### 📊 Complexity Analysis
| Type | Complexity | Justification |
| :--- | :--- | :--- |
| **Time** | $O(n)$ | Splitting takes linear time, and the relative distance lookups process each character exactly once. |
| **Space** | $O(n)$ | Tokenizing the string into split session segments scales proportionally with the input length. |

### 🛠️ Technical Details
- **Pattern:** String Tokenization / Fixed-Array Relative Index Mapping


## 🧪 Testing
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.
- **Edge Cases Handled:**
    - **Empty String / Only Asterisks (`****`):** Returns `0` immediately.
    - **Active Window Shifts (`test_duplicate_within_same_session`):** Validates that the window correctly shrinks and shifts forward when an active collision occurs.
    - **Out-of-Window Duplicates (`test_duplicate_outside_active_window`):** Uses relative distance logic to ignore stale (`s1`), or historical index (`s0`) entries sitting safely behind the active window.