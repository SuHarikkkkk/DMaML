from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)

    if g != 1:
        return None

    return x % m


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def solve_two_congruences(a1, m1, a2, m2):
    g = gcd(m1, m2)

    if (a2 - a1) % g != 0:
        return None, None

    m1_div = m1 // g
    m2_div = m2 // g
    diff = (a2 - a1) // g

    inv = mod_inverse(m1_div, m2_div)

    if inv is None:
        return None, None

    t = (diff * inv) % m2_div

    lcm = m1 * m2_div
    x = (a1 + m1 * t) % lcm

    return x, lcm


def solve_congruence_system():
    n = int(input("Введите количество сравнений: "))

    residues = []
    moduli = []

    for i in range(n):
        print(f"\nСравнение №{i + 1}")
        a = int(input("Введите остаток a: "))
        m = int(input("Введите модуль m: "))

        if m <= 0:
            print("Модуль должен быть положительным.")
            return

        residues.append(a)
        moduli.append(m)

    x = residues[0]
    m = moduli[0]

    for i in range(1, n):
        x, m = solve_two_congruences(x, m, residues[i], moduli[i])

        if x is None:
            print("\nСистема не имеет решений.")
            return

    print(f"x ≡ {x} (mod {m})")

def rsa_encrypt_decrypt():
    phrase = "Четные числа - питательные, а нечетные - просто вкусные"

    print("\nМожно использовать стандартные значения p = 61, q = 53")
    choice = input("Ввести свои p и q? да/нет: ").lower()

    if choice == "да":
        p = int(input("Введите простое число p: "))
        q = int(input("Введите простое число q: "))
    else:
        p = 61
        q = 53

    if not is_prime(p) or not is_prime(q):
        print("Ошибка: p и q должны быть простыми числами.")
        return

    if p == q:
        print("Ошибка: p и q должны быть разными.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17

    while gcd(e, phi) != 1:
        e += 1

    d = mod_inverse(e, phi)

    if d is None:
        print("Не удалось найти закрытый ключ.")
        return

    data = phrase.encode("utf-8")

    if n <= 255:
        print("\nОшибка: n должно быть больше 255 для шифрования байтов.")
        return

    encrypted = []

    for byte in data:
        c = pow(byte, e, n)
        encrypted.append(c)

    print(encrypted)

    decrypted_bytes = []

    for c in encrypted:
        m = pow(c, d, n)
        decrypted_bytes.append(m)

    decrypted_phrase = bytes(decrypted_bytes).decode("utf-8")

    print(decrypted_phrase)


def main():
    while True:
        print("\n========== МЕНЮ ==========")
        print("1. Решить систему сравнений")
        print("2. RSA-шифрование фразы")
        print("0. Выход")
        print("==========================")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            solve_congruence_system()
        elif choice == "2":
            rsa_encrypt_decrypt()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню.")


main()