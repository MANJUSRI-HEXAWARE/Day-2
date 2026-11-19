from collections import deque


class HubNetwork:
    def __init__(self, routes):
        self.routes = {hub: list(neighbors) for hub, neighbors in routes.items()}
        for neighbors in list(self.routes.values()):
            for hub in neighbors:
                self.routes.setdefault(hub, [])
    def shortest_route(self, start, destination):
        if start not in self.routes or destination not in self.routes:
            return []
        queue = deque([(start, [start])])
        visited = {start}
        while queue:
            hub, path = queue.popleft()
            if hub == destination:
                return path
            for neighbor in self.routes[hub]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []

    def reachable(self, start):
        if start not in self.routes:
            return []
        visited = set()
        result = []

        def dfs(hub):
            visited.add(hub)
            result.append(hub)
            for neighbor in self.routes[hub]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result


if __name__ == "__main__":
    routes = {
        "DEL": ["JAI", "LKO", "AMD"],
        "JAI": ["DEL", "AMD"],
        "LKO": ["DEL", "KOL"],
        "AMD": ["DEL", "JAI", "MUM"],
        "MUM": ["AMD", "PUN", "HYD"],
        "PUN": ["MUM", "BLR"],
        "HYD": ["MUM", "BLR", "CHE"],
        "BLR": ["PUN", "HYD", "CHE"],
        "CHE": ["HYD", "BLR", "KOL"],
        "KOL": ["LKO", "CHE"]
    }
    network = HubNetwork(routes)
    print("Adjacency list:")
    for hub, neighbors in network.routes.items():
        print(f"{hub}: {', '.join(neighbors)}")
    route = network.shortest_route("DEL", "CHE")
    print("Shortest DEL to CHE:", " -> ".join(route))
    print("Fewest hops:", len(route) - 1 if route else "Unreachable")
    print("DFS reachable from DEL:", network.reachable("DEL"))
