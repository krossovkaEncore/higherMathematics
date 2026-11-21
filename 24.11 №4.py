G = 9.8
INITIAL_HEIGHT = 100
TOTAL_TIME = 2


def simulate(dt, update_velocity_first):
    height = INITIAL_HEIGHT
    velocity = 0
    steps = round(TOTAL_TIME / dt)

    for _ in range(steps):
        if update_velocity_first:
            velocity -= G * dt
            height += velocity * dt
        else:
            height += velocity * dt
            velocity -= G * dt

    return height


exact = INITIAL_HEIGHT - 0.5 * G * TOTAL_TIME**2

print(f"Точная высота: {exact:.6f} м\n")

for dt in (0.1, 0.001):
    print(f"Шаг времени: {dt}")

    height1 = simulate(dt, False)
    height2 = simulate(dt, True)

    print(f"Сначала высота:   {height1:.6f} м")
    print(f"Сначала скорость: {height2:.6f} м")
    print(f"Точная формула:   {exact:.6f} м")
    print()
