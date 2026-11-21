import random


def calculate_pi(n):
    inside = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= 1:
            inside += 1

    return 4 * inside / n


for n in (10**3, 10**4, 10**5, 10**6):
    pi = calculate_pi(n)
    error = abs(math.pi - pi)

    print(f"n = {n:>7}: π ≈ {pi:.7f}, ошибка = {error:.7f}")
