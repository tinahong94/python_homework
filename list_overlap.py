import random
a = random.sample(range(15), 10)
b = random.sample(range(15), 10)
c = []
for number in a:
    if number in b:
        c.append(number)

print(sorted(a))
print(sorted(b))
print(sorted(c))
