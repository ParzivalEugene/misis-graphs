with open("INPUT.txt", "r", encoding="utf-8") as file:
    data = [list(map(int, row.split())) for row in file.read().split("\n")]
    n, m, data = *data[0], data[1:]
    traffic_ligths = [0] * n

    for i in range(m):
        x, y = data[i]
        traffic_ligths[x - 1] += 1
        traffic_ligths[y - 1] += 1

    with open("OUTPUT.txt", "w", encoding="utf-8") as file:
        file.write(" ".join(map(str, traffic_ligths)))
