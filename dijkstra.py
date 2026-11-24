"""Dijkstra shortest paths for a non-negative weighted graph."""
import heapq
def build_graph(edges):
    graph = {}
    for a, b, w in edges:
        graph.setdefault(a, []).append((b, w))
        graph.setdefault(b, []).append((a, w))
    return graph
def dijkstra(graph, start):
    dist = {v: float("inf") for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        d, u = heapq.heappop(queue)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v], prev[v] = nd, u
                heapq.heappush(queue, (nd, v))
    return dist, prev
def reconstruct_path(prev, start, end):
    path, node = [], end
    while node is not None:
        path.append(node)
        if node == start:
            break
        node = prev.get(node)
    path.reverse()
    return path if path and path[0] == start else []
