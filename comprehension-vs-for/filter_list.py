MILLION_NUMBERS = list(range(1_000_000))


def for_loop():
    # sourcery skip: inline-immediately-returned-variable, list-comprehension
    output = []
    output.extend(element for element in MILLION_NUMBERS if not element % 2)
    return output

# run with timeit
# python -m timeit -s "from filter_list import for_loop" "for_loop()"
