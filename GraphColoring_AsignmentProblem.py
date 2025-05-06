from collections import deque


def dfs(filename, start_node=0):
    def read_file(filename):
        graph = {}
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    parts = line.strip().split(":")
                    node = int(parts[0])
                    neighbor = (
                        list(map(int, parts[1].strip().split()))
                        if parts[1].strip()
                        else []
                    )
                    graph[node] = neighbor
        return graph

    def dfs_run(graph, node, visited):
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_run(graph, neighbor, visited)

    graph = read_file(filename)
    visited = set()
    print("DFS:")
    dfs_run(graph, start_node, visited)


def bfs(filename, start_node=0):
    def read_file(filename):
        graph = {}
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    parts = line.strip().split(":")
                    node = int(parts[0])
                    neighbor = (
                        list(map(int, parts[1].strip().split()))
                        if parts[1].strip()
                        else []
                    )
                    graph[node] = neighbor
        return graph

    graph = read_file(filename)
    visited = set()
    visited.add(start_node)
    queue = deque([start_node])

    print("BFS:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def graphColoring(filename):
    def read_graph(filename):
        graph = {}
        with open(filename, "r") as f:
            for line in f:
                if ":" in line:
                    parts = line.strip().split(":")
                    node = int(parts[0])
                    neighbor = (
                        list(map(int, parts[1].strip().split()))
                        if parts[1].strip()
                        else []
                    )
                    graph[node] = neighbor
        return graph

    graph = read_graph(filename)
    n = len(graph)
    color = [-1] * n
    degree = [len(graph[i]) for i in range(n)]
    visited = [False] * n

    for _ in range(n):
        max_pos = -1
        u = -1
        for i in range(n):
            if degree[i] > max_pos and not visited[i]:
                max_pos = degree[i]
                u = i
        if u == -1:
            break

        visited[u] = True

        neighbor = []

        for i in graph.get(u, []):
            if color[i] != -1:
                neighbor.append(color[i])

        c = 1
        while c in neighbor:
            c += 1
        color[u] = c

        for v in graph.get(u, []):
            if not visited[v]:
                degree[v] -= 1
    print("Run Graph Coloring: ")
    for i in color:
        print(i, end=" ")


def AssignmentProblem(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        n, m = map(int, lines[0].split(" "))
        time = list(map(int, lines[1].split(" ")))

    work = [0] * m
    graph = {i: [] for i in range(m)}

    for _ in range(n):
        max_ele = -1
        for i in range(n):
            if max_ele < time[i]:
                max_ele = time[i]
                u = i

        min_ele = float("inf")
        for i in range(m):
            if min_ele > work[i]:
                min_ele = work[i]
                v = i

        work[v] += time[u]
        time[u] = -1

        graph[v].append(u)

    for i in graph:
        print("Máy", i, ": ", end="")
        for j in graph.get(i, []):
            print(j, end=" ")
        print("\n")


if __name__ == "__main__":
    AssignmentProblem("graph.txt")
