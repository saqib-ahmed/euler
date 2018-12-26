from functools import reduce
import numpy as np


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


abundant_numbers = []

for num in range(2, 28124):
    facts = factors(num)
    facts.remove(num)
    facts_sum = np.array(list(facts)).sum()
    if facts_sum > num:
        abundant_numbers.append(num)

np_abundant = np.array(abundant_numbers)
total_sum = 0
all_sums = [0]*28124
for i in np_abundant:
    for j in abundant_numbers:
        if i+j > 28123:
            break
        all_sums[i+j] = i+j


for i in range(1, 28124):
    if all_sums[i] == 0:
        total_sum += i

print(total_sum)
