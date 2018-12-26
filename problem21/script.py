from functools import reduce
import numpy as np


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


total_sum = 0
for num in range(2, 10000):
    facts = factors(num)
    facts.remove(num)
    sum_of_factors = np.array(list(facts)).sum()
    facts_amicable = factors(sum_of_factors)
    facts_amicable.remove(sum_of_factors)
    sum_of_amicable_factors = np.array(list(facts_amicable)).sum()
    if num == sum_of_amicable_factors and num != sum_of_factors:
        total_sum += num

print(total_sum)
