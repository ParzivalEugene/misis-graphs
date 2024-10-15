def min_weight_path(matrix, m, n):
    dp = [[float("inf")] * n for _ in range(m)]
    path = [[[] for _ in range(n)] for _ in range(m)]

    for i in range(m):
        dp[i][0] = matrix[i][0]
        path[i][0] = [i + 1]

    for j in range(1, n):
        for i in range(m):
            for ni in (i - 1, i, i + 1):
                if 0 <= ni < m:
                    new_weight = dp[ni][j - 1] + matrix[i][j]
                    if new_weight < dp[i][j]:
                        dp[i][j] = new_weight
                        path[i][j] = path[ni][j - 1] + [i + 1]
                    elif (
                        new_weight == dp[i][j]
                        and path[ni][j - 1] + [i + 1] < path[i][j]
                    ):
                        path[i][j] = path[ni][j - 1] + [i + 1]

    min_weight = float("inf")
    min_path = []
    for i in range(m):
        if dp[i][n - 1] < min_weight:
            min_weight = dp[i][n - 1]
            min_path = path[i][n - 1]

    return min_path, min_weight


with open("INPUT.TXT", "r") as f:
    m, n = map(int, f.readline().split())
    matrix = [list(map(int, f.readline().split())) for _ in range(m)]

min_path, min_weight = min_weight_path(matrix, m, n)

with open("OUTPUT.TXT", "w") as f:
    f.write(" ".join(map(str, min_path)) + "\n")
    f.write(str(min_weight) + "\n")
