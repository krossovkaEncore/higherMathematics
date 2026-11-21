import math


def integral(f, a, b, n):
    h = (b - a) / n
    total = sum(
        f(a + (i + 0.5) * h)
        for i in range(n)
    )
    return total * h


result1 = integral(math.sin, 0, math.pi, 1000)
result2 = integral(lambda x: x**2, 0, 1, 1000)

print(f"Интеграл sin(x): {result1:.8f}")
print(f"Интеграл x²:     {result2:.8f}")

print(f"Ожидаемый результат 1: {2}")
print(f"Ожидаемый результат 2: {1 / 3:.8f}")
