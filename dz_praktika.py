import time


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def test_gcd(a, b):
    start_time = time.perf_counter()
    result = gcd(a, b)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f"НОД({a}, {b}) = {result}")
    print(f"Время выполнения: {elapsed_time:.10f} секунд\n")


# Тесты
test_gcd(100, 5)
test_gcd(10 ** 5, 500)
test_gcd(10 ** 6, 5 * 10 ** 3)