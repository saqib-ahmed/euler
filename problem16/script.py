
num = 2**1000
s = 0
while num:
    s += num % 10
    num //= 10

print(s)
