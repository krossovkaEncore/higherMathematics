import random


def monte_carlo_pi(N):
    inside = 0

    for _ in range(N):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            inside += 1

    return 4 * inside / N


random.seed(42)

for N in (100, 10**4, 10**6):
    print(N, monte_carlo_pi(N))
