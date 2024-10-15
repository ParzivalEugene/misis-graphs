with open("INPUT.TXT") as f:
    n = int(f.readline())
    steps = list(map(int, f.readline().split()))

dp = [0] * n

prev = [-1] * n

dp[0] = steps[0]
if n > 1:
    dp[1] = max(steps[0] + steps[1], steps[1])
    prev[1] = 0 if dp[1] == steps[0] + steps[1] else -1

for i in range(2, n):
    if dp[i - 1] > dp[i - 2]:
        dp[i] = dp[i - 1] + steps[i]
        prev[i] = i - 1
    else:
        dp[i] = dp[i - 2] + steps[i]
        prev[i] = i - 2

max_sum = dp[n - 1]

path = []
i = n - 1
while i >= 0:
    path.append(i + 1)
    i = prev[i]

path.reverse()

with open("OUTPUT.TXT", "w") as f:
    f.write(str(max_sum) + "\n")
    f.write(" ".join(map(str, path)) + "\n")
