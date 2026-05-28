# Max Unique Substring Length in a Session

## I. Solutions

### 🚀 Quick Comparison Matrix
| Solutions & Approaches | Time | Space |
| :--- | :--- | :--- |
| **s0:** Sliding Window + Index Tracking | $O(n)$ | $O(\min(n, \Sigma))$ |
| **s1:** String Split + Relative Distance Mapping | $O(n)$ | $O(n)$ |

---

### 1. Sliding Window + Index Tracking

#### 💡 Intuition & Approach
We scan the string linearly using a **Sliding Window**. Characters matching `*` act as hard **session walls**. 

When a wall is hit, we instantly reset tracking by clearing the hash map and shifting our starting boundary (`pivot`) past the wall. For valid characters, a hash map tracks their last seen index. If a duplicate appears within the active session, `pivot` safely jumps past its previous occurrence to maintain a window of unique characters.

#### 🛠️ Technical Details
- **Pattern:** Sliding Window / Hash Map Index Tracking

#### 📊 Complexity Analysis
- **Time** $O(n)$: The string is processed in a single linear pass with $O(1)$ map operations.
- **Space** $O(\min(n, \Sigma))$: The map stores at most the total number of unique characters ($\Sigma$) within one session.

### 2. String Split + Relative Distance Mapping

#### 💡 Intuition & Approach
This solution uses `.split('*')` to isolate clean session segments, tracking each character's last seen index inside a fixed-size array of size 26.

Rely on relative-distance mathematics. If the distance between the current index `i` and the character's last seen index is strictly greater than `window_size`, the previous duplicate is mathematically guaranteed to sit outside the current active window. This allows `window_size` to safely expand without triggering a false collision.

#### 🛠️ Technical Details
- **Pattern:** String Tokenization / Fixed-Array Relative Index Mapping

#### 📊 Complexity Analysis
- **Time** $O(n)$: Splitting takes linear time, and the relative distance lookups process each character exactly once.
- **Space** $O(n)$: Tokenizing the string into split session segments scales proportionally with the input length.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.

### 🛡️ Edge Cases Coverage
- **[Stream Boundaries]:** Assures correct evaluation of empty strings or inputs containing nothing but session walls (`****`), verifying the system defaults to a length of `0` without throwing unexpected exceptions.
- **[Session Isolation Traps]:** Validates character tracking across multi-session environments separated by hard walls (`*`), ensuring unique window lengths are reset properly and do not bleed into neighboring sessions.
- **[Window Collision Dynamics]:** Verifies sliding boundaries during close-range duplicates within a single session (e.g., `"abcad"` and `"abba"`), ensuring old index pointers are safely bypassed or updated without breaking window logic.