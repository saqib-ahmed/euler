
def find_chain(num):
    a = [num]

    while num != 1:
        if num % 2 == 0:
            num = num/2
            a.append(num)
        else:
            num = (3 * num)+1
            a.append(num)
    return len(a)


x = 2
number = 2
for i in range(2, 1000000):
    if find_chain(i) > x:
        x = find_chain(i)
        number = i

print(x)
print(number)
