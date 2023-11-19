import sys

num = int(input("Please enter a number (n > 0) -> "))
if num < 0 :
    raise Exception("Invalid number")

max = -sys.maxsize
for i in range(num):
    number = int(input("Enter number -> "))
    if max < number:
        max = number


print(f"Biggest number is {max}")