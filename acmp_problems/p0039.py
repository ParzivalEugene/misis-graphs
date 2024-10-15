def max_profit(n, prices):
    total_profit = 0
    max_price_ahead = 0

    for i in range(n - 1, -1, -1):
        max_price_ahead = max(max_price_ahead, prices[i])
        total_profit += max_price_ahead

    return total_profit


with open("INPUT.TXT", "r") as f:
    n = int(f.readline().strip())
    prices = list(map(int, f.readline().split()))

with open("OUTPUT.TXT", "w") as f:
    f.write(str(max_profit(n, prices)))
