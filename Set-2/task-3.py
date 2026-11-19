from collections import deque
def shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return None
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == target:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return None
def has_cycle(graph):
    states = {}
    def visit(node):
        states[node] = 1
        for neighbor in graph[node]:
            if states.get(neighbor) == 1:
                return True
            if states.get(neighbor, 0) == 0 and visit(neighbor):
                return True
        states[node] = 2
        return False
    return any(visit(node) for node in graph if states.get(node, 0) == 0)
if __name__ == "__main__":
    stages = {
        "Registration": ["Assessment"],
        "Assessment": ["Surveyor", "Settlement"],
        "Surveyor": ["Settlement"],
        "Settlement": [],
    }
    print("Shortest path Registration to Settlement:", shortest_path(stages, "Registration", "Settlement"))
    print("Cycle in approval graph:", has_cycle(stages))
    with_loop = {key: neighbors.copy() for key, neighbors in stages.items()}
    with_loop["Settlement"].append("Assessment")
    print("Cycle after Settlement to Assessment:", has_cycle(with_loop))
