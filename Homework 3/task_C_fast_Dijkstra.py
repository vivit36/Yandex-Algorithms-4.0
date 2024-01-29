import heapq


def dijkstra(vertexes, start, finish):
    n = len(vertexes) - 1
    visited = [False] * (n + 1)

    heap_dist = []
    heapq.heapify(heap_dist)
    heapq.heappush(heap_dist, (float('inf'), start))

    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    while len(heap_dist) != 0:
        cur = heapq.heappop(heap_dist)
        if visited[cur[1]] is False:
            visited[cur[1]] = True
            dist[cur[1]] = cur[0]
            for next_vertex in vertexes[cur[1]]:
                heapq.heappush(heap_dist, (cur[0] + next_vertex[1], next_vertex[0]))

    return dist[finish] if dist[finish] != float('inf') else -1


def main():
    n, m = map(int, input().strip().split())
    vertexes = [dict() for _ in range(n + 1)]
    for i in range(m):
        a, b, t, w = map(int, input().strip().split())
        vertexes[a][b] = [t, (w - 3000000) // 100]
        vertexes[b][a] = vertexes[a][b]

    print(dijkstra(vertexes, 1, n))


if __name__ == '__main__':
    main()