def subsetSumToK(n, k, arr):
    t = [[False for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][k]
