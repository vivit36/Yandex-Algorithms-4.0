
def dijkstra_for_bus(vertexes, begin, end):
    def find_min(time_lst, vis_lst):
        min_v = float('inf')
        ind = -1
        for i in range(1, len(time_lst)):
            if vis_lst[i] is False and time_lst[i] < min_v:
                min_v = time_lst[i]
                ind = i
        return ind

    n = len(vertexes) - 1
    visited = [False] * (n + 1)
    dist = [float('inf')] * (n + 1)
    dist[begin] = 0
    cur = begin

    while cur != -1:
        visited[cur] = True
        for next_vertex in vertexes[cur]:
            if next_vertex[1] >= dist[cur] and dist[next_vertex[0]] > next_vertex[2]:
                dist[next_vertex[0]] = next_vertex[2]

        cur = find_min(dist, visited)

    return dist[end] if dist[end] != float('inf') else -1


def main():
    n = int(input().strip())
    d, v = map(int, input().strip().split())
    r = int(input().strip())

    vertexes = [[] for _ in range(n + 1)]
    for i in range(r):
        start, s_time, finish, f_time = map(int, input().strip().split())
        vertexes[start].append((finish, s_time, f_time))

    print(dijkstra_for_bus(vertexes, d, v))


if __name__ == '__main__':
    main()