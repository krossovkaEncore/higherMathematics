import heapq


def dijkstra(graph, start):
    distances = {v: float("inf") for v in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current, u = heapq.heappop(heap)

        if current > distances[u]:
            continue

        for v, weight in graph[u]:
            new_distance = current + weight

            if new_distance < distances[v]:
                distances[v] = new_distance
                heapq.heappush(heap, (new_distance, v))

    return distances


graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("C", 2), ("D", 1)],
    "C": [("A", 1), ("B", 2), ("D", 5)],
    "D": [("B", 1), ("C", 5)]
}

print(dijkstra(graph, "A"))

graph["A"].append(("D", 3))
graph["D"].append(("A", 3))

print(dijkstra(graph, "A"))
