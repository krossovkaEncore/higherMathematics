def max_events(events):
    events = sorted(events, key=lambda p: p[1])
    chosen = []
    end = -1

    for start, finish in events:
        if start >= end:
            chosen.append((start, finish))
            end = finish

    return chosen


events = [
    (1, 4), (3, 5), (0, 6), (5, 7),
    (3, 9), (5, 9), (6, 10), (8, 11),
    (8, 12), (2, 14), (12, 16)
]

print(max_events(events))


def shortest_events(events):
    events = sorted(events, key=lambda p: p[1] - p[0])
    chosen = []

    for event in events:
        if all(
            event[1] <= x[0] or event[0] >= x[1]
            for x in chosen
        ):
            chosen.append(event)

    return chosen


example = [(1, 5), (4, 7), (6, 10)]

print(shortest_events(example))
