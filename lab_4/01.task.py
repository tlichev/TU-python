n = int(input("Please enter a number -> "))
numbers = []
[numbers.append(n) for n in range(1, n +1)]

print(f"Increasing order - > {', '.join(map(str, numbers))}")
print(f"Decreasing order -> {', '.join(map(str,numbers[::-1]))}")