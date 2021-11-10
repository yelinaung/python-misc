MILLION_NUMBERS = list(range(1_000_000))


def list_comprehension():
    return [number for number in MILLION_NUMBERS if not number % 2]


# run as
# python -m timeit -s "from filter_list import list_comprehension" "list_comprehension()"
