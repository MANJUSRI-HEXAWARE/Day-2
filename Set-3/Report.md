

## 1. Algorithm Decision Table

| Task | Data Structure / Pattern | Reason | Time Complexity | Auxiliary Space |
|---|---|---|---|---|
| Hub insertion and search | Binary Search Tree | Ordered hub codes and efficient average-case lookup | Average O(log n), worst O(n) per operation | O(h) recursive insert; O(1) iterative search |
| BST traversals and height | DFS tree traversal | Inorder yields sorted codes; height measures longest root-to-leaf path | O(n) | O(h) recursion, plus O(n) output |
| Parcel lookup and repeat scans | Dictionary and set (hashing) | Fast tracking-number lookup and repeated `(parcel, hub)` detection | Average O(1), worst O(n) per lookup/scan | O(p+s) |
| Fewest-hop hub route | Breadth-First Search | Finds shortest path by edge count in an unweighted graph | O(V(V+E)) worst case with path copying; standard BFS O(V+E) | O(V²) worst case for queued full paths |
| Reachable hubs | Depth-First Search | Visits every reachable hub | O(V+E) | O(V) |
| Peak four-hour window | Sliding window | Reuses previous sum instead of recomputing each four-hour total | O(n) | O(1) |
| Palindrome of hub codes | Two pointers | Compares codes symmetrically from both ends | O(n) | O(n) for tokenization |

Here, `n` is the input size, `h` is BST height, `p` is the number of parcels, `s` is the number of distinct scans, `V` is the number of hubs, and `E` is the number of routes. Hashing complexities are expected averages. BFS could use O(V+E) auxiliary space by storing parent links rather than full paths.

## 2. Task 1 – Hub Binary Search Tree

The BST stores ten unique hub codes. Inorder traversal produces sorted hub codes. Height is reported in **edges**: an empty tree has height -1 and a single-node tree has height 0. Sorted insertion into an ordinary, unbalanced BST creates a skewed tree with height `n-1`, making lookup O(n) in the worst case.

**Program:** `01_Hub_BST.py`

**Execution output:**

```text
Insertion order: ['HYD', 'DEL', 'MUM', 'BLR', 'GOA', 'KOL', 'PUN', 'AMD', 'CHE', 'JAI']
Search CHE: True
Search LKO: False
Inorder: ['AMD', 'BLR', 'CHE', 'DEL', 'GOA', 'HYD', 'JAI', 'KOL', 'MUM', 'PUN']
Preorder: ['HYD', 'DEL', 'BLR', 'AMD', 'CHE', 'GOA', 'MUM', 'KOL', 'JAI', 'PUN']
Postorder: ['AMD', 'CHE', 'BLR', 'GOA', 'DEL', 'JAI', 'KOL', 'PUN', 'MUM', 'HYD']
Tree height (edges): 3
Sorted-input height (edges): 9
```

## 3. Task 2 – Parcel Tracking Hash Map

The dictionary maps tracking numbers to destinations. A set of `(tracking number, normalized hub)` pairs detects repeated scans at the same hub, while allowing the same parcel to be scanned at a different hub. Python handles hash collisions internally using equality checks and its dictionary/set collision-resolution mechanisms.

**Program:** `02_Parcel_Hash_Map.py`

**Execution output:**

```text
Lookup TRK1001: Chennai
Lookup TRK9999: None
TRK1001 at HYD: Scan recorded
TRK1001 at hyd: Duplicate scan
TRK1001 at BLR: Scan recorded
TRK9999 at HYD: Unknown parcel
```

## 4. Task 3 – Hub Routing Graph

The adjacency list represents ten hubs and direct, bidirectional routes. BFS returns a route with the fewest hops because each route counts as one edge. DFS lists all hubs reachable from the central depot, DEL.

**Program:** `03_Hub_Routing_Graph.py`

**Execution output:**

```text
Adjacency list:
DEL: JAI, LKO, AMD
JAI: DEL, AMD
LKO: DEL, KOL
AMD: DEL, JAI, MUM
MUM: AMD, PUN, HYD
PUN: MUM, BLR
HYD: MUM, BLR, CHE
BLR: PUN, HYD, CHE
CHE: HYD, BLR, KOL
KOL: LKO, CHE
Shortest DEL to CHE: DEL -> LKO -> KOL -> CHE
Fewest hops: 3
DFS reachable from DEL: ['DEL', 'JAI', 'AMD', 'MUM', 'PUN', 'BLR', 'HYD', 'CHE', 'KOL', 'LKO']
```

## 5. Task 4 – Highest-Average Delivery Window

A sliding window adds the new hour and subtracts the departing hour. The four-hour interval is reported as start-inclusive and end-exclusive. Ties are resolved by choosing the earliest window.

**Program:** `04_Delivery_Window.py`

**Execution output:**

```text
Hourly parcel counts: [120, 135, 110, 145, 160, 190, 240, 280, 310, 295, 270, 250, 230, 260, 340, 390, 420, 400, 350, 300, 260, 210, 180, 150]
Highest-average 4-hour window: 15:00-19:00
Average parcels per hour: 390.00
```

## 6. Task 5 – Route Palindrome

The route is tokenized into alphabetic hub codes, then normalized to uppercase. Two pointers compare entire hub codes from both ends, ignoring case, spaces, arrows, commas, and slashes. An empty route is considered a palindrome by the conventional definition.

**Program:** `05_Route_Palindrome.py`

**Execution output:**

```text
'DEL -> MUM -> HYD -> mum -> del': True
'DEL, MUM, HYD, CHE': False
'BLR / HYD / BLR': True
'': True
```

## 7. Verification Cases

| Task | Case | Expected Result |
|---|---|---|
| BST | Search missing hub | False |
| BST | Insert duplicate hub | No duplicate node |
| BST | Sorted insertion | Height increases to n-1 |
| Hash map | Same parcel scanned twice at same hub with different case | Duplicate scan |
| Hash map | Same parcel scanned at a different hub | Scan recorded |
| Hash map | Unknown tracking number | Unknown parcel |
| Graph | Start equals destination | One-hub route, zero hops |
| Graph | Unreachable destination | Empty route |
| Sliding window | Fewer than four hourly counts | No valid window |
| Sliding window | Exactly four hourly counts | One valid window |
| Palindrome | Mixed case and separators | Correct palindrome result |
| Palindrome | Nonmatching hub codes | False |

