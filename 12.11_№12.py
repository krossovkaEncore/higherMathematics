def run_turing(program, tape_str, start="q1", stop="q0",
               blank="_", max_steps=1000, trace=False):
    tape = {i: ch for i, ch in enumerate(tape_str)}
    pos = 0
    state = start
    steps = 0
    shift = {"L": -1, "R": 1, "N": 0}

    while state != stop and steps < max_steps:
        symbol = tape.get(pos, blank)
        if (state, symbol) not in program:
            raise ValueError(f"Нет команды для ({state}, {symbol!r})")
        if trace:
            print(steps, state, symbol, "позиция", pos)
        new_symbol, move, state = program[(state, symbol)]
        tape[pos] = new_symbol
        pos += shift[move]
        steps += 1

    left, right = min(tape), max(tape)
    result = "".join(tape.get(i, blank) for i in range(left, right + 1))
    return result.strip(blank), steps

INC = {
    ("q1", "0"): ("0", "R", "q1"),
    ("q1", "1"): ("1", "R", "q1"),
    ("q1", "_"): ("_", "L", "q2"),
    ("q2", "1"): ("0", "L", "q2"),
    ("q2", "0"): ("1", "N", "q0"),
    ("q2", "_"): ("1", "N", "q0"),
}


if __name__ == "__main__":
    for n in range(21):
        result, _ = run_turing(INC, bin(n)[2:])
        expected = bin(n + 1)[2:]
        assert result == expected, (n, result, expected)

    print("Все тесты для n от 0 до 20 пройдены.")
