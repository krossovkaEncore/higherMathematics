import math


def left_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def middle_rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))


def trapezoids(f, a, b, n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2

    total += sum(f(a + i * h) for i in range(1, n))
    return total * h


def integrate(method, f, a, b, n):
    match method:
        case "left":
            return left_rectangles(f, a, b, n)
        case "middle":
            return middle_rectangles(f, a, b, n)
        case "trapezoid":
            return trapezoids(f, a, b, n)
        case _:
            raise ValueError("Неизвестный метод")


methods = ["left", "middle", "trapezoid"]
exact = 2

print(f"{'n':<8} {'Метод':<15} {'Значение':<15} {'Ошибка'}")

for n in (10, 100, 1000):
    for method in methods:
        result = integrate(method, math.sin, 0, math.pi, n)
        error = abs(exact - result)

        print(f"{n:<8} {method:<15} {result:<15.10f} {error:.10f}")

    print()
