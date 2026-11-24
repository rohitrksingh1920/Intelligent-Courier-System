"""Nearest-Neighbor approximation for a TSP-style delivery tour."""
def nearest_neighbor_route(start, destinations, distance):
    unvisited, route, total, current = set(destinations), [start], 0, start
    while unvisited:
        nxt = min(unvisited, key=lambda v: (distance(current, v), v))
        leg = distance(current, nxt)
        if leg == float("inf"):
            raise ValueError("A destination is unreachable.")
        route.append(nxt); total += leg
        unvisited.remove(nxt); current = nxt
    back = distance(current, start)
    if back == float("inf"):
        raise ValueError("The depot is unreachable from the final stop.")
    route.append(start)
    return route, total + back
