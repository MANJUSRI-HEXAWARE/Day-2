# Set 2 – Insurance Claims Processing

**Business Scenario:** Claim approval routing, duplicate claim detection, and claim spike monitoring.

## Implementation Summary

Five Python programs were implemented and executed. An automated test suite verified normal, empty-input, duplicate, and boundary cases. Sample claim records and daily counts were used because no source dataset was supplied.

## Decision and Complexity Table

| Task | Data Structure / Pattern | Reason | Time Complexity | Auxiliary Space |
|---|---|---|---|---|
| 1. Claim ID insertion and search | Binary Search Tree | Maintains ordered claim IDs and supports searching | Insert/search O(h), average O(log n), worst O(n); traversals O(n) | O(n) stored nodes; O(h) traversal stack |
| 2. Duplicate claim detection | Hash map with normalized composite key | Case/whitespace variations map to the same policy/date key | Expected O(n) for n claims, assuming bounded key length; worst-case O(n²) with pathological collisions | O(n) |
| 3. Approval route and cycle detection | Directed adjacency-list graph, BFS and DFS | BFS finds shortest path by edges; DFS detects back edges | O(V + E) per traversal | O(V + E) including graph; O(V) auxiliary traversal state, with parent pointers |
| 4. Consecutive high-claim days | Sliding window / consecutive-run scan | Finds longest contiguous run where claims > 100 | O(n) | O(1) |
| 5. Merge regional claims | Two pointers | Merges already sorted lists without re-sorting | O(n + m) | O(n + m) for merged output; O(1) auxiliary beyond output |

For the BST, h is tree height. Inorder traversal produces ascending claim IDs. A plain BST is not self-balancing.

## Duplicate-Detection Rule

A claim is treated as a duplicate when its policy number matches after removing whitespace and case-folding and its incident date matches after ISO date normalization. Different claim IDs do not prevent detection. This is a business-rule match, not a general fuzzy similarity algorithm.

Python dictionaries handle hash collisions internally by comparing keys for equality after locating candidate hash slots. Two distinct keys with the same hash do not become duplicates unless their normalized key values are equal. Duplicate claims are returned as pairs of current and first-seen claim IDs. The implementation assumes valid ISO-format incident dates.

## Graph Rule

Approval stages use directed edges: Registration → Assessment, Assessment → Surveyor, Surveyor → Settlement, with an additional direct Assessment → Settlement route. BFS returns the shortest route by number of edges, not processing time. Adding Settlement → Assessment creates a cycle detected by DFS.

## Sliding Window Rule

A high-claim day requires **strictly more than 100 claims**. A day with exactly 100 ends the current run. Day numbers in the result are one-based. If two runs have equal maximum length, the first is returned.

## Test Coverage

The test suite includes BST empty traversal/search, duplicate insertion, found/missing claims, duplicate detection with case and spacing differences, different incident dates, empty and unreachable graphs, directed cycles and self-loops, empty and threshold-boundary claim sequences, tied windows, empty merges, and duplicate-preserving merges.

## Actual Execution Output

### 01_Claim_BST.py

```text
Inorder (sorted): [1010, 1025, 1030, 1040, 1045, 1050, 1060, 1075, 1080, 1090]
Preorder: [1050, 1025, 1010, 1040, 1030, 1045, 1075, 1060, 1090, 1080]
Postorder: [1010, 1030, 1045, 1040, 1025, 1060, 1080, 1090, 1075, 1050]
Search 1040: True
Search 9999: False
Insert duplicate 1040: False
```

### 02_Duplicate_Claims.py

```text
Duplicate (claim, original) pairs: [('CL002', 'CL001'), ('CL004', 'CL003')]
Empty input: []
```

### 03_Approval_Graph.py

```text
Shortest path Registration to Settlement: ['Registration', 'Assessment', 'Settlement']
Cycle in approval graph: False
Cycle after Settlement to Assessment: True
```

### 04_Claim_Spike_Window.py

```text
Daily claims: [80, 110, 125, 140, 90, 105, 130, 160, 115, 145, 100, 120, 135]
Longest run (days): 5
From day: 6
Through day: 10
Empty input: (0, None, None)
```

### 05_Merge_Claims.py

```text
North office: [1001, 1004, 1008, 1012, 1012]
South office: [1002, 1004, 1009, 1015]
Merged claims: [1001, 1002, 1004, 1004, 1008, 1009, 1012, 1012, 1015]
Empty inputs: []
```

### 06_Test_Cases.py

```text
PASS: BST empty traversals
PASS: BST empty search
PASS: BST insertion
PASS: BST duplicate rejected
PASS: BST sorted inorder
PASS: BST preorder and postorder
PASS: BST found and missing
PASS: Hashing empty input
PASS: Hashing case and spacing duplicates
PASS: Hashing different incident dates
PASS: Graph empty path
PASS: Graph empty cycle
PASS: Graph BFS shortest path
PASS: Graph unreachable path
PASS: Graph same-stage path
PASS: Graph acyclic
PASS: Graph DFS cycle
PASS: Graph self-loop
PASS: Sliding window empty input
PASS: Sliding window strict threshold
PASS: Sliding window longest run
PASS: Sliding window first tie
PASS: Merge both empty
PASS: Merge one empty
PASS: Merge preserves duplicates
PASS: Merge negative and positive
All 26 tests passed.
```

## Result

All five task programs ran successfully. The test suite completed with **26 of 26 tests passed**.
