from matplotlib import pyplot as plt

import time


def compute_time_to_add(list_to_add_to, item):
    start = time.perf_counter()
    list_to_add_to.append(item)
    end = time.perf_counter()
    return end-start


timings = []
some_list = []
values = range(10_000_000)
for n in values:
    timings.append(compute_time_to_add(some_list, n))

plt.plot(values, timings)
plt.show()