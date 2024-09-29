with open("INPUT.txt", "r", encoding="utf-8") as file:
    raw = file.read().split("\n")
    n = int(raw[0])
    bridges, hills = [raw[i].split() for i in range(1, n + 1)], raw[-2].split()

    bad_bridges = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bridges[i][j] == "1" and hills[i] != hills[j]:
                bad_bridges += 1

with open("OUTPUT.txt", "w", encoding="utf-8") as file:
    file.write(str(bad_bridges))
