import random

numbers = []

for n in range(1):
    numbers.insert(random.randint(1,100),1)
    numbers.insert(random.randint(1,100),1)
    numbers.insert(random.randint(1,100),1)
    print(numbers)
    numbers.remove(numbers[0]) 
    numbers.append(random.randint(1,100))
    numbers.append(random.randint(1,100))
    numbers.sort()
    print(numbers)
    numbers.pop()
    numbers.reverse()
    print(numbers)