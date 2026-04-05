import numpy as np
import ast
from collections import deque, defaultdict

# 1. БУЛЕВЫ МАТРИЦЫ
def input_matrix():
    return np.array(ast.literal_eval(input("Введите матрицу: ")))

def disjunction(A, B):
    return ((A + B) > 0).astype(int)

def boolean_product(A, B):
    return (A @ B > 0).astype(int)

def transpose(A):
    return A.T

def invert(A):
    return (A == 0).astype(int)

def subtract(A, B):
    return A - B

def multiply(A, B):
    return A @ B

# 2. ТОПОЛОГИЧЕСКАЯ СОРТИРОВКА

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([v for v in vertices if in_degree[v] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(vertices):
        print("Ошибка: граф содержит цикл")
        return None

    return order

# 3. ГРУППА СИММЕТРИЙ ШЕСТИУГОЛЬНИКА (D6)

def compose(p, q):
    return tuple(p[i-1] for i in q)

def generate_D6():
    # вершины 1..6
    rotation = (2, 3, 4, 5, 6, 1)
    reflection = (1, 6, 5, 4, 3, 2)

    elements = set()
    current = (1, 2, 3, 4, 5, 6)

    # вращения
    for _ in range(6):
        elements.add(current)
        current = compose(rotation, current)

    # отражения
    refls = set()
    for r in elements:
        refls.add(compose(reflection, r))

    return list(elements | refls)

def cayley_table(elements):
    table = []
    for a in elements:
        row = []
        for b in elements:
            row.append(compose(a, b))
        table.append(row)
    return table

def check_abelian(elements):
    for a in elements:
        for b in elements:
            if compose(a, b) != compose(b, a):
                return False
    return True

# МЕНЮ

def menu():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Операции над матрицами")
        print("2. Топологическая сортировка")
        print("3. Группа симметрий шестиугольника")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            A = input_matrix()
            B = input_matrix()

            print("\n1. Дизъюнкция")
            print(disjunction(A, B))

            print("\n2. Булево умножение")
            print(boolean_product(A, B))

            print("\n3. Транспонирование")
            print(transpose(A))

            print("\n4. Инвертирование")
            print(invert(A))

            print("\n5. Вычитание")
            print(subtract(A, B))

            print("\n6. Умножение")
            print(multiply(A, B))


        elif choice == "2":
            vertices = ast.literal_eval(input("Введите вершины: "))
            edges = ast.literal_eval(input("Введите рёбра (пары): "))

            order = topological_sort(vertices, edges)
            if order:
                print("Топологический порядок:", order)


        elif choice == "3":
            elements = generate_D6()

            print("\nЭлементы группы (как подстановки):")
            for e in elements:
                print(e)

            print("\nТаблица умножения:")
            table = cayley_table(elements)
            for row in table:
                print(row)

            print("\nГруппа абелева?")
            print("Да" if check_abelian(elements) else "Нет")


        elif choice == "0":
            break

        else:
            print("Неверный выбор")


menu()