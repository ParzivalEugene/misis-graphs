with open("INPUT.txt", "r", encoding="utf-8") as file:
    raw = file.read().split("\n")
    n = int(raw[0])
    matrix = [list(map(int, raw[i].split())) for i in range(1, n + 1)]

    min_route = 3000
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                route = matrix[i][j] + matrix[j][k] + matrix[k][i]
                if route < min_route:
                    min_route = route

with open("OUTPUT.txt", "w", encoding="utf-8") as file:
    file.write(str(min_route))
