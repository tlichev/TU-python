number = int(input())

flag = True
for i in range(2, number):
    if number % 2 == 0:
        flag = False

if flag:
    print(f"Number is prime")
else:
    print(f"Number is not prime")