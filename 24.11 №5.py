import math


def midpoint_integral(f, a, b, n):
    h = (b - a) / n

    return h * sum(
        f(a + (i + 0.5) * h)
        for i in range(n)
    )


limit = 10**-8

n = math.floor(math.sqrt(1 / (12 * limit))) + 1

result = midpoint_integral(lambda x: x**2, 0, 1, n)

exact = 1 / 3
error = abs(exact - result)

print(f"Количество разбиений: {n}")
print(f"Вычисленный интеграл: {result:.12f}")
print(f"Точное значение:      {exact:.12f}")
print(f"Ошибка:               {error:.12e}")
print(f"Требуемая точность:   {limit:.12e}")
print(f"Условие выполнено:    {error < limit}")
