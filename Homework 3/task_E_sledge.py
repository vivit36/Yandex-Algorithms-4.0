class Town:
    def __init__(self, name, wait, speed):
        self.name = name
        self.wait = wait
        self.speed = speed
        self.neigh = dict()


def dijkstra_sledge(town_lst, town_matr, start):
    def find_min(arr, vis):
        min_v = float('inf')
        ind = -1
        for i in range(1, len(arr)):
            if vis[i] is False and arr[i] < min_v:
                min_v = arr[i]
                ind = i
        return ind

    dist = [float('inf')] * len(town_matr)
    visited = [False] * len(town_matr)
    path = [0] * len(town_matr)
    path[start] = -1
    cur = 1
    dist[cur] = 0

    while cur != -1:
        visited[cur] = True
        for i, town_dist in enumerate(town_matr[cur][1:], 1):
            if i != cur and town_dist != 0:
                travel_time = dist[cur] + town_dist / town_lst[i].speed + town_lst[i].wait
                if dist[i] > travel_time:
                    dist[i] = travel_time
                    path[i] = cur

        cur = find_min(dist, visited)

    max_dist = 0
    ind = -1
    for i in range(1, len(dist)):
        if dist[i] > max_dist:
            max_dist = dist[i]
            ind = i

    res = list()
    res.append(ind)
    cur = path[ind]
    while cur != -1:
        res.append(cur)
        cur = path[cur]

    return dist[ind], list(reversed(res))


def bfs(town_lst, buffer):

    for i in range(1, len(town_lst)):
        start_vertex = town_lst[i]
        visited = [False] * len(town_lst)
        queue = list()
        for el in start_vertex.neigh.keys():
            queue.append(town_lst[el])
        visited[i] = True

        while len(queue) != 0:
            cur_vertex = queue.pop(0)
            visited[cur_vertex.name] = True
            for next_vertex, dist in cur_vertex.neigh.items():
                if visited[next_vertex] is False:
                    if next_vertex not in start_vertex.neigh:
                        if cur_vertex.name not in start_vertex.neigh:
                            buffer[start_vertex.name][next_vertex] = buffer[start_vertex.name][cur_vertex.name] + dist
                        else:
                            buffer[start_vertex.name][next_vertex] = start_vertex.neigh[cur_vertex.name] + dist
                    queue.append(town_lst[next_vertex])

    return buffer


def main():
    n = int(input().strip())
    town_lst = [0]
    for i in range(1, n + 1):
        t, v = map(int, input().strip().split())
        town_lst.append(Town(i, t, v))

    town_matr = [[0] * len(town_lst) for _ in range(len(town_lst))]

    for i in range(n - 1):
        a, b, s = map(int, input().strip().split())
        town_matr[a][b] = s
        town_matr[b][a] = s
        town_lst[a].neigh[b] = s
        town_lst[b].neigh[a] = s

    town_matr = bfs(town_lst, town_matr)

    ans = dijkstra_sledge(town_lst, town_matr, 1)
    print(ans[0])
    print(' '.join(map(str, reversed(ans[1]))))


if __name__ == '__main__':
    main()