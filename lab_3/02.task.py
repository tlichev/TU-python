

num = int(input("Please enter a number (n > 0) -> "))
if num < 0 :
    raise Exception("Invalid number")

sum = 0
for i in range(num):
    number = int(input("Enter number -> "))
    sum += number

print("-"*20)
print(f"Sum is {sum}")
print("-"*20)
