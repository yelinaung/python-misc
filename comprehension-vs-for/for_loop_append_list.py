output = []
MILLION_NUMBERS = list(range(1_000_000))


def for_loop():
    for element in MILLION_NUMBERS:
        output.append(element)

    return output
