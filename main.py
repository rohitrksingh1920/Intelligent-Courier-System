"""Main demonstration for the Intelligent Courier Planning System."""
from parcel_sorting import merge_sort_parcels
from knapsack import select_parcels_knapsack
from dijkstra import build_graph, dijkstra, reconstruct_path
from tsp_optimization import nearest_neighbor_route
from sample_data import DEPOT, VEHICLE_CAPACITY, PARCELS, EDGES
from performance_testing import run_performance_tests

def main():
    print("="*60)
    print("INTELLIGENT COURIER PLANNING SYSTEM")
    print("="*60)

    print("\nPHASE 2 - PACKAGE PRIORITIZATION AND BOX FILLING")
    ordered = merge_sort_parcels(PARCELS)
    print("Sorted parcels (deadline, priority):")
    for p in ordered:
        print(f'{p["id"]}: destination={p["destination"]}, weight={p["weight"]}kg, deadline={p["deadline"]}, priority={p["priority"]}')
    chosen, weight, value, dp = select_parcels_knapsack(ordered, VEHICLE_CAPACITY)
    print(f"Vehicle capacity: {VEHICLE_CAPACITY} kg")
    print("Selected:", ", ".join(p["id"] for p in chosen))
    print(f"Packed weight: {weight} kg; priority value: {value}")
    print("Knapsack DP table:")
    for row in dp:
        print(" ".join(map(str, row)))

    print("\\nPHASE 3 - ROUTE MAKER AND GRAPH PROCESSING")
    graph = build_graph(EDGES)
    print("Graph adjacency list:")
    for node in sorted(graph):
        print(node, graph[node])
    destinations = sorted({p["destination"] for p in chosen})
    stops = [DEPOT] + destinations
    dist_maps, prev_maps = {}, {}
    for source in stops:
        dist_maps[source], prev_maps[source] = dijkstra(graph, source)
    for dest in destinations:
        path = reconstruct_path(prev_maps[DEPOT], DEPOT, dest)
        print(f"Shortest path to {dest}: {' -> '.join(path)} = {dist_maps[DEPOT][dest]} km")
    route, route_km = nearest_neighbor_route(DEPOT, destinations, lambda a,b: dist_maps[a][b])
    print("Approximate route:", " -> ".join(route))
    print("Total route distance (including return):", route_km, "km")
    for a,b in zip(route, route[1:]):
        path = reconstruct_path(prev_maps[a], a, b)
        print(f"Leg {a} to {b}: {' -> '.join(path)} ({dist_maps[a][b]} km)")

    print("\\nPHASE 4 - PERFORMANCE TESTING")
    print("Parcels Capacity Sorting_ms Knapsack_ms")
    for count, cap, sort_ms, pack_ms in run_performance_tests(PARCELS):
        print(f"{count} {cap} {sort_ms:.4f} {pack_ms:.4f}")

    print("\\nPHASE 5 - SUMMARY")
    print("Packing, shortest-path calculation, and approximate route planning completed.")
    print("Nearest Neighbor is a heuristic; it does not guarantee the globally shortest tour.")

if __name__ == "__main__":
    main()
