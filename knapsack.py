"""0/1 Knapsack dynamic programming."""
def select_parcels_knapsack(parcels, capacity):
    n = len(parcels)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p = parcels[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if p["weight"] <= c:
                dp[i][c] = max(dp[i][c], p["priority"] + dp[i - 1][c-p["weight"]])
    selected, remaining = [], capacity
    for i in range(n, 0, -1):
        if dp[i][remaining] != dp[i-1][remaining]:
            p = parcels[i-1]
            selected.append(p)
            remaining -= p["weight"]
    selected.reverse()
    return selected, sum(p["weight"] for p in selected), sum(p["priority"] for p in selected), dp
