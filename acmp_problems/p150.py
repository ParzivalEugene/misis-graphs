def dfv(i):
    visited[i] = True
    for j in range(n):
        if matrix[i][j] == 1 and not visited[j]:
            dfv(j)


with open("INPUT.txt", "r", encoding="utf-8") as file:
    raw = file.read().split("\n")
    n, s = map(int, raw[0].split())
    matrix = [list(map(int, raw[i].split())) for i in range(1, n + 1)]

    visited = [False] * n
    dfv(s - 1)

with open("OUTPUT.txt", "w", encoding="utf-8") as file:
    file.write(str(visited.count(True) - 1))
