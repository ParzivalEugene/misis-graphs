with open("INPUT.txt", "r", encoding="utf-8") as file:
    n, x, y = map(int, file.read().split("\n")[:-1])

    while x != y:
        if x > y:
            x //= 2
        else:
            y //= 2

with open("OUTPUT.txt", "w", encoding="utf-8") as file:
    file.write(str(x))
