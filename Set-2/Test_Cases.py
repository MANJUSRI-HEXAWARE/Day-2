import importlib.util
from pathlib import Path

def load(filename, name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parent / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tests():
    bst = load("01_Claim_BST.py", "bst")
    hashing = load("02_Duplicate_Claims.py", "hashing")
    graph = load("03_Approval_Graph.py", "graph")
    window = load("04_Claim_Spike_Window.py", "window")
    merge = load("05_Merge_Claims.py", "merge")
    count = 0

    def check(condition, label):
        nonlocal count
        assert condition, label
        count += 1
        print("PASS:", label)

    tree = bst.ClaimBST()
    check(tree.inorder() == [] and tree.preorder() == [] and tree.postorder() == [], "BST empty traversals")
    check(not tree.search(5), "BST empty search")
    check(tree.insert(5) and tree.insert(3) and tree.insert(7), "BST insertion")
    check(not tree.insert(3), "BST duplicate rejected")
    check(tree.inorder() == [3, 5, 7], "BST sorted inorder")
    check(tree.preorder() == [5, 3, 7] and tree.postorder() == [3, 7, 5], "BST preorder and postorder")
    check(tree.search(7) and not tree.search(8), "BST found and missing")

    check(hashing.find_duplicates([]) == [], "Hashing empty input")
    records = [
        {"claim_id": "A", "policy_number": "Ab 12", "incident_date": "2026-11-01"},
        {"claim_id": "B", "policy_number": "a b 12", "incident_date": " 2026-11-01 "},
        {"claim_id": "C", "policy_number": "AB12", "incident_date": "2026-11-02"},
        {"claim_id": "D", "policy_number": "AB12", "incident_date": "2026-11-01"},
    ]
    check(hashing.find_duplicates(records) == [("B", "A"), ("D", "A")], "Hashing case and spacing duplicates")
    check(hashing.claim_key(records[0]) != hashing.claim_key(records[2]), "Hashing different incident dates")

    empty_graph = {}
    check(graph.shortest_path(empty_graph, "A", "B") is None, "Graph empty path")
    check(not graph.has_cycle(empty_graph), "Graph empty cycle")
    network = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    check(graph.shortest_path(network, "A", "D") == ["A", "B", "D"], "Graph BFS shortest path")
    check(graph.shortest_path(network, "D", "A") is None, "Graph unreachable path")
    check(graph.shortest_path(network, "A", "A") == ["A"], "Graph same-stage path")
    check(not graph.has_cycle(network), "Graph acyclic")
    check(graph.has_cycle({"A": ["B"], "B": ["A"]}), "Graph DFS cycle")
    check(graph.has_cycle({"A": ["A"]}), "Graph self-loop")

    check(window.longest_claim_spike([]) == (0, None, None), "Sliding window empty input")
    check(window.longest_claim_spike([100, 99, 20]) == (0, None, None), "Sliding window strict threshold")
    check(window.longest_claim_spike([101, 102, 100, 103, 104, 105]) == (3, 4, 6), "Sliding window longest run")
    check(window.longest_claim_spike([101, 102, 90, 105, 106]) == (2, 1, 2), "Sliding window first tie")

    check(merge.merge_sorted_claims([], []) == [], "Merge both empty")
    check(merge.merge_sorted_claims([], [1, 2]) == [1, 2], "Merge one empty")
    check(merge.merge_sorted_claims([1, 3, 3], [2, 3, 4]) == [1, 2, 3, 3, 3, 4], "Merge preserves duplicates")
    check(merge.merge_sorted_claims([-3, 0], [-2, 5]) == [-3, -2, 0, 5], "Merge negative and positive")

    print(f"All {count} tests passed.")


if __name__ == "__main__":
    run_tests()
