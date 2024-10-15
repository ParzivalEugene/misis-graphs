import heapq


with open("INPUT.TXT") as file:
    n, s, f = map(int, file.readline().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, file.readline().split())))


s -= 1
f -= 1


def dijkstra(graph, start, end):
    dist = [float("inf")] * len(graph)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u == end:
            return current_dist

        if current_dist > dist[u]:
            continue

        for v in range(len(graph)):
            if graph[u][v] != -1:
                next_dist = current_dist + graph[u][v]
                if next_dist < dist[v]:
                    dist[v] = next_dist
                    heapq.heappush(pq, (next_dist, v))

    return -1


result = dijkstra(graph, s, f)


if result == float("inf"):
    result = -1


with open("OUTPUT.TXT", "w") as file:
    file.write(str(result) + "\n")
