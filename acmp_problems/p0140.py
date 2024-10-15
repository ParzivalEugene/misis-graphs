INF = 100000


def has_negative_cycle(n, graph):
    for start in range(n):
        dist = [INF] * n
        dist[start] = 0

        for _ in range(n - 1):
            for u in range(n):
                for v in range(n):
                    if graph[u][v] != INF and dist[u] != INF:
                        if dist[v] > dist[u] + graph[u][v]:
                            dist[v] = dist[u] + graph[u][v]

        for u in range(n):
            for v in range(n):
                if graph[u][v] != INF and dist[u] != INF:
                    if dist[v] > dist[u] + graph[u][v]:
                        return True
    return False


with open("INPUT.TXT") as f:
    n = int(f.readline())
    graph = []
    for i in range(n):
        graph.append(list(map(int, f.readline().split())))

if has_negative_cycle(n, graph):
    with open("OUTPUT.TXT", "w") as f:
        f.write("YES\n")
else:
    with open("OUTPUT.TXT", "w") as f:
        f.write("NO\n")
