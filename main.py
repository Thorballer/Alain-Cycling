from fractions import Fraction

a = int(input("Input the 'a' term: "))
b = int(input("Input the 'b' term: "))
c = int(input("Input the 'c' term: "))
k = int(input("Input the 'k' term: "))

A = (a**b) % k
print(f'A = {A}')
B = (a**b) % c
print(f'B = {B}')
d = abs((A-B))
print(f'd = {d}')

n = 0
if A > B:
    while True:
        w = (c**n) % k
        print(f'For n: {n}, value is {w} ')
        if w == d:
            q = (c**n)
            print(f"value to add to B (q): {q}")
            q = (B+q) / c
            print(f"Decimal value is: {q}")
            q = Fraction(q).limit_denominator()
            print(f'Fraction answer is: {q}')
            break

        else:
            if n >= 100:
                print("You're cooked chat, it doesn't work")
                print("Better grab the calc (calc is short for calulator)")
                break

            n+=1
elif B >= A:
    while True:
        w = (k ** n) % c
        print(f'For n: {n}, value is {w} ')
        if w == d:
            q = (k ** n)
            print(f"value to add to A (q): {q}")
            q = (q + A) / c
            print(f"Decimal value is: {q}")
            q = Fraction(q).limit_denominator()
            print(f'Fraction answer is: {q}')
            break
        else:
            if n >= 100:
                print("You're cooked chat, it doesn't work")
                print("Better grab the calc (calc is short for calulator)")
                break

            n += 1