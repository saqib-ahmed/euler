
file = open("./p022_names.txt").read()
arr = [i for i in file.split(',')]
arr.sort()
total_sum = 0

for index, val in enumerate(arr):
    individual_sum = 0
    for letter in val:
        if letter != "\"":
            individual_sum += ord(letter.lower())-96
    total_sum += (individual_sum * (index + 1))

print(total_sum)
