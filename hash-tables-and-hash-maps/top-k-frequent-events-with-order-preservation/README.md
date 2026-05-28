# Top K Frequent Events with Order Preservation

## I. Solutions

### 🚀 Quick Comparison Matrix
| Solutions & Approaches | Time | Space |
| :--- | :--- | :--- |
| **s0:** Dual-Map Hashing (Frequency + First Appearance) | $O(n + u \log u)$ | $O(u)$ |

---

### 1. Dual-Map Hashing (Frequency + First Appearance)

#### 💡 Intuition & Approach
To solve this problem while strictly preserving arrival order during ties, we decouple tracking into two specialized hash maps:
1. A **frequency map** to count element occurrences.
2. A **first-appearance map** to log the exact index where an element is first encountered.

The core mechanism relies on a compound sorting key. By sorting the frequency in a **descending** fashion (using a negative value trick) and the initial appearance index in an **ascending** fashion, we naturally group elements by highest frequency while seamlessly breaking ties using historical arrival order.

#### 🛠️ Technical Details
- **Pattern:** Hash Map Frequency Counting / Index Tracking / Compound Sorting Key

#### 📊 Complexity Analysis
- **Time** $O(n + u \log u)$: Building the hash maps requires a single linear pass of $O(n)$. Sorting the collection of unique elements ($u$) takes $O(u \log u)$ time.
- **Space** $O(u)$: Two tracking maps allocate memory proportional only to the number of unique elements ($u$) present in the input stream.


## II. Testing & Edge Cases

### 🧪 Testing Strategy
This problem is verified using a suite of unit tests following the **AAA (Arrange-Act-Assert)** pattern.
- `test_solution.py`: Contains standard, edge, and boundary test cases.

### 🛡️ Edge Cases Coverage
- **[Stream Boundaries]:** Features dedicated test cases for single events and empty arrays to verify that the system handles minimal bounds without throwing exceptions.
- **[Order Preservation Traps]:** Includes a scrambled insertion order test case where all events share identical frequencies, ensuring the system strictly honors historical arrival order over default numerical sorting.