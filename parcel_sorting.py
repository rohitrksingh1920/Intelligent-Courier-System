"""Merge Sort: earliest deadline first, then highest priority."""
def merge_sort_parcels(parcels):
    if len(parcels) <= 1:
        return parcels[:]
    mid = len(parcels) // 2
    left, right = merge_sort_parcels(parcels[:mid]), merge_sort_parcels(parcels[mid:])
    result, i, j = [], 0, 0
    def key(p):
        return (p["deadline"], -p["priority"], p["id"])
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
