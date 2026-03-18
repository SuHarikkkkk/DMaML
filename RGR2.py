from collections import deque, defaultdict


def topological_sort(vertices, edges):
    # граф и входящие степени
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    # заполняем граф
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # очередь вершин без входящих рёбер
    queue = deque([v for v in vertices if in_degree[v] == 0])

    linear_order = []

    while queue:
        current = queue.popleft()
        linear_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(linear_order) != len(vertices):
        raise ValueError("Граф содержит цикл, топологическая сортировка невозможна")

    return linear_order
