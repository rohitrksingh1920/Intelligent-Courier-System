"""Average runtime tests for sorting and packing on 6, 12, and 24 parcels."""
from time import perf_counter
from parcel_sorting import merge_sort_parcels
from knapsack import select_parcels_knapsack
def run_performance_tests(parcels, repeats=20):
    results = []
    for multiplier, capacity in ((1,15),(2,30),(4,60)):
        data = []
        for copy_no in range(multiplier):
            for p in parcels:
                q = p.copy()
                q["id"] = f'{p["id"]}_{copy_no+1}'
                data.append(q)
        start = perf_counter()
        for _ in range(repeats):
            ordered = merge_sort_parcels(data)
        sort_ms = (perf_counter()-start)*1000/repeats
        start = perf_counter()
        for _ in range(repeats):
            select_parcels_knapsack(ordered, capacity)
        pack_ms = (perf_counter()-start)*1000/repeats
        results.append((len(data), capacity, sort_ms, pack_ms))
    return results
