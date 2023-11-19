import random

n = int(input("Please enter a size of List -> "))

RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'


numbers = []
for _ in range(n):
    numbers.append(random.randint(1,10))
print(f"Original list->  {' '.join(map(str, numbers))} ")



idx = 1
while idx < len(numbers):
    res = numbers[idx] + numbers[idx-1]
    numbers.insert(idx, res)
    idx += 2


print("Extended list -> ", end="")
for i in range(len(numbers)):
    if i % 2 != 0:
        print(RED + f"{numbers[i]}" + RESET, end=" ")
    else:
        print(BLUE + f"{numbers[i]}" + RESET, end=" ")

