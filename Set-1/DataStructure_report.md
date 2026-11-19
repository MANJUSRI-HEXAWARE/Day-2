# Execution Report – E-Commerce Catalogue and Traffic Analysis
## Execution Results

The following outputs were captured by executing the Python programs. Task 2 timing values depend on the machine and may vary between runs.

### Task 1 – 

```text
Total categories: 15
Search Electronics: True
Search Appliances: False
Inorder: Automotive, Beauty, Books, Electronics, Fashion, Furniture, Grocery, Health, Home, Jewelry, Music, Pet Supplies, Sports, Stationery, Toys
Preorder: Grocery, Electronics, Beauty, Automotive, Books, Fashion, Furniture, Sports, Health, Home, Jewelry, Music, Pet Supplies, Toys, Stationery
Postorder: Automotive, Books, Beauty, Furniture, Fashion, Electronics, Pet Supplies, Music, Jewelry, Home, Health, Stationery, Toys, Sports, Grocery
```

### Task 2 – 

```text
Collision bucket: 1
Chained entries: [['SKU-00001', 'Rice'], ['SKU-00006', 'Sugar']]
Lookup SKU-00006: Sugar
SKU records: 100000
Queries per round: 10000
Custom matches across rounds: 70000
Dictionary matches across rounds: 70000
Custom chained table median: 4.067 ms
Built-in dictionary median: 1.510 ms
Faster in this run: Built-in dictionary
```

### Task 3 – `03_Microservice_Graph.py`

```text
Valid deployment order (BFS topological sort):
Catalogue -> User -> Inventory -> Pricing -> Payment -> Cart -> Checkout -> Notification
Cycle test: Circular dependency detected
```

### Task 4 – `04_Peak_Traffic.py`

```text
Hourly RPM: [120, 100, 90, 85, 95, 140, 210, 330, 450, 540, 620, 700, 760, 820, 900, 860, 730, 650, 580, 480, 390, 300, 220, 160]
Busiest 3-hour window: 13:00 to 16:00
Total requests in window: 154800
Average RPM during peak: 860
Peak hourly RPM: 900
```

### Task 5 – `05_Two_Pointer_Pairs.py`

```text
Sorted order values: [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
Gift-card target: 1000
Matching distinct value pairs: [(150, 850), (200, 800), (250, 750), (300, 700), (350, 650), (400, 600), (450, 550)]
Total pairs: 7
```

## Decision Table

| Task | Problem | Data Structure / Pattern | Reason | Time Complexity |
|---|---|---|---|---|
| 1 | Insert, find, and traverse 15 product categories | Binary Search Tree | Supports ordered traversal and search; inorder returns sorted categories | Insert/search O(h), traversal O(n); worst-case h = n |
| 2 | Fast SKU look-up and collision handling | Hash table with separate chaining; Python dictionary | Buckets resolve collisions; dictionary provides optimized hash-map lookups | Expected O(1) lookup, worst-case O(n) |
| 3 | Deploy microservices respecting prerequisites and detect cycles | Directed graph + Kahn's BFS topological sort | Each dependency deploys before its dependent service; a cycle prevents a complete topological order | O(V + E) (excluding sorting for deterministic output) |
| 4 | Find busiest consecutive 3-hour period | Fixed-size sliding window | Reuses previous window total instead of summing each window again | O(n) |
| 5 | Find unique value pairs matching a gift-card amount | Two pointers on sorted list | Moves pointers inward based on sum; skips duplicates | O(n) |

## Key Findings

**Task 1:** Fifteen categories were inserted into the BST. Search results and inorder, preorder, and postorder traversals were produced.

**Task 2:** `SKU-00001` and `SKU-00006` collided in a five-bucket table and were retained through separate chaining. A custom table and Python dictionary were benchmarked using 100,000 stored SKUs and 10,000 lookups per round, with the median of seven rounds reported. This is a small illustrative benchmark, not a rigorous performance study.

**Task 3:** The deployment graph uses `service: [prerequisites]`. The BFS topological order satisfies the prerequisite relationships, including Pricing and Inventory before Cart. Adding Checkout as a prerequisite for Catalogue creates a cycle, which the program detects.

**Task 4:** The 24 input values represent average requests per minute during each one-hour interval. Each hourly value is multiplied by 60 before summing a three-hour window. The calculation assumes the stated RPM is constant within its hour.

**Task 5:** The two-pointer method returns each distinct pair of **values** once. If duplicate order amounts occur, it does not enumerate separate order-ID combinations.



No third-party packages are required.
