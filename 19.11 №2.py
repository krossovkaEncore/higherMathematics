def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    steps = 0

    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2

        if a[mid] == x:
            return mid, steps
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1, steps


a = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary_search(a, 23))
print(binary_search(a, 7))
