total = int(input("How many values? "))
numbers = []
for _ in range(total):
    numbers.append(int(input()))

sum_even = 0
count_odd = 0

for x in numbers:
    if x % 2 == 0:
        sum_even += x
    else:
        count_odd += 1

first = numbers[:]

second = numbers[:]
second.append(sum_even)

third = numbers[:]
third.insert(1, count_odd)

fourth = third[:3]

print(first)
print(second)
print(third)
print(fourth)
