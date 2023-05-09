import time

from classes.helper import Helper
from classes.multidimensional_array_handler import MultidimensionalArrayHandler


def make_timer(callback, *args):
    start = time.perf_counter_ns()
    elem = callback(*args)
    end = time.perf_counter_ns()
    print(f"{callback.__name__}: Spent time {end - start} nanoseconds")
    print(f"number of additions: {helper.additions}, number of multiplications: {helper.multiplications}\n")
    helper.additions, helper.multiplications = 0, 0
    return elem


matrix = [
    [
        ['A', 'B'],
        ['C', 'D'],
        ['E', 'F'],
    ],
    [
        ['G', 'H'],
        ['I', 'J'],
        ['K', 'L'],
    ],
    [
        ['M', 'N'],
        ['O', 'P'],
        ['Q', 'R'],
    ]
]
index_intervals = ((0, 2), (0, 2), (0, 1))
dimension = 3
indices = (2, 2, 1)

helper = Helper()
handler = MultidimensionalArrayHandler(matrix, dimension, index_intervals)

make_timer(handler.direct_access, indices, helper.mul_with_count, helper.sum_with_count)
make_timer(handler.access_by_ilifee_vectors, indices, helper.sum_with_count)
make_timer(handler.access_by_defining_vector, indices, helper.mul_with_count, helper.sum_with_count)
