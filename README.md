# Intelligent Courier Planning System
Beginner-friendly Python capstone prototype.

## Run
Python 3.8+; no external dependencies. In this folder run:
`python main.py`

## Files and algorithms
- parcel_sorting.py: Merge Sort by earliest deadline, then highest priority. O(p log p).
- knapsack.py: 0/1 Knapsack DP maximizing total priority under capacity. O(p*C) time and space.
- dijkstra.py: adjacency-list graph and heap-based Dijkstra. O((V+E) log V) per source.
- tsp_optimization.py: Nearest-Neighbor route approximation; returns to depot.
- performance_testing.py: average sorting and Knapsack times for 6, 12, 24 parcels.
- sample_data.py: editable sample parcels, capacity, and road distances.
- main.py: runs the full demonstration.

## Data assumptions
Parcel fields: id, destination, weight (whole kg), deadline (lower means sooner), priority (higher is more valuable).
Road edges are undirected triples (location A, location B, distance km) with non-negative weights.
The vehicle starts and ends at DEPOT. Each selected destination is visited once.

## Limitations
One vehicle and one trip are modelled. No live traffic, time windows, parcel volume, or multiple trips.
Nearest Neighbor is an approximation, not a guaranteed optimal TSP solution.
Future work: 2-opt improvement, one-dimensional Knapsack DP, time windows, multiple vehicles,
traffic-aware edge weights, and shortest-path caching.
