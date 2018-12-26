
import numpy as np
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


nums = [i for i in range(1,1000000)]
np_nums = np.array(nums)

for i in range(1, 1000000):
    triangle_number = np_nums[0: i].sum()
    num_divisors = len(factors(triangle_number))

    if num_divisors > 500:
        print(triangle_number)
        exit(0)
