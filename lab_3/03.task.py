n = int(input("Please enter n (n > 0) -> "))
if n < 0 :
    raise Exception("Invalid number")

for i in range(n+1):
    print("*" * i)
