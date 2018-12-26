def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)


s = 0
res = factorial(100)
while res:
    s += res % 10
    res //= 10

print(s)
