import numpy as np


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())

import math

all_v = 0
for i in range(1, N):
    if i == 1:
        all_v += 1
        continue
    rets = prime_factorize(i)
    d = {}
    for ret in rets:
        if ret not in d.keys():
            d[ret] = 1
        else:
            d[ret] += 1

    total = 1
    for k, v in d.items():
        total *= v + 1
    # print(f"i=={i}, total={total}")
    all_v += total
print(all_v)
