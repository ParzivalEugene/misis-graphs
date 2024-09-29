with open("INPUT.TXT", "r", encoding="utf-8") as file:
    data = file.read().split("\n")
    n, data = int(data[0]), data[1:]
    counter = 0
    for i, row in enumerate(data):
        counter += row.replace(" ", "")[i:n].count("1")
with open("OUTPUT.TXT", "w", encoding="utf-8") as file:
    file.write(str(counter))
