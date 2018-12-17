import random

a = ['abc', 1, 2, 3, 'def']
x = random.choice(a)
print(x)
for _ in range(10):
    print(random.randint(5, 8))
