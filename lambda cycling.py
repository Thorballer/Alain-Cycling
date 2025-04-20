import math
from fractions import Fraction
from primefactor import primefactors

def carmichael(n):
    # 1) prime‑factor n
    counts = {}
    for p in primefactors(n):
        counts[p] = counts.get(p, 0) + 1

    # 2) compute λ(p^e) for each prime power
    lam = 1
    for p, e in counts.items():
        if p == 2:
            if   e == 1: pe_lam = 1
            elif e == 2: pe_lam = 2
            else:        pe_lam = 2 ** (e-2)
        else:
            # p odd: λ(p^e) = p^(e-1) * (p−1)
            pe_lam = (p-1) * p**(e-1)

        lam = math.lcm(lam, pe_lam)

    return lam

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
k = int(input("k: "))

n = c * k
l = carmichael(n)

b_mod = b % l

from fractions import Fraction
print("as a reduced fraction:", Fraction(a**b_mod, c))
