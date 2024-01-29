def dijkstra(vertexes, start, finish):
    def find_min(arr, vis):
        min_v = 100 * (len(arr) - 1) + 1
        ind = -1
        for i in range(1, len(arr)):
            if vis[i] is False and arr[i] < min_v:
                min_v = arr[i]
                ind = i
        return ind

    n = len(vertexes) - 1
    visited = [False] * (n + 1)
    dist = [100 * n + 1] * (n + 1)
    path = [0] * (n + 1)
    path[start] = -1
    dist[start] = 0
    cur = start
    while cur != -1:
        visited[cur] = True
        for next_vertex in vertexes[cur]:
            if dist[next_vertex[0]] > dist[cur] + next_vertex[1]:
                dist[next_vertex[0]] = dist[cur] + next_vertex[1]
                path[next_vertex[0]] = cur
        cur = find_min(dist, visited)

    if path[finish] != 0:
        res = list()
        res.append(finish)
        cur = path[finish]
        while cur != -1:
            res.append(cur)
            cur = path[cur]
        return ' '.join(map(str, reversed(res)))
    else:
        return -1


def main():
    n, s, f = map(int, input().strip().split())
    vertexes = [[] for x in range(n + 1)]
    for i in range(1, n + 1):
        neigh = [int(x) for x in input().strip().split(' ')]
        for j in range(n):
            if neigh[j] > 0:
                vertexes[i].append((j + 1, neigh[j]))
    print(dijkstra(vertexes, s, f))


if __name__ == '__main__':
    main()