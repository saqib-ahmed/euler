def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)


def combination(x, y):
    return factorial(x) / (factorial(x-y)*factorial(y))


res = combination(2*20, 20)

print(res)
