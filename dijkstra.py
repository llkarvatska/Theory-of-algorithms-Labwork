import heapq
import math

graph = {
    1: {2: 2, 4: 7, 7: 5},
    2: {1: 2, 5: 9},
    3: {7: 9, 4: 4, 6: 4, 8: 4},
    4: {1: 7, 5: 2, 6: 5, 3: 4},
    5: {2: 9, 4: 2, 6: 3},
    6: {4: 5, 5: 3, 3: 4, 8: 1},
    7: {1: 5, 3: 9, 8: 6},
    8: {7: 6, 6: 1, 3: 4}
}

def dijkstra(graph, start):
    dist = {v: math.inf for v in graph}
    pred = {v: -1 for v in graph}
    dist[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u].items():
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred

dist, pred = dijkstra(graph, 1)

print("dist =", dist)
print("pred =", pred)
