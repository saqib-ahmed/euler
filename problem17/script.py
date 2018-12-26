import inflect


def get_letters(num):
    string = p.number_to_words(num)
    string = string.replace('-', '')
    string = string.replace(' ', '')
    return len(string)


p = inflect.engine()
s = 0
for i in range(1, 1001):
    s += get_letters(i)

print(s)
