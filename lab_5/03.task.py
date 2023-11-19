def calculator(operation):

    match operation:
        case "+":
            a = int(input("Enter first num -> "))
            b = int(input("Enter second num -> "))
            return a+b
        case "-":
            a = int(input("Enter first num -> "))
            b = int(input("Enter second num -> "))
            return a-b
        case "*":
            a = int(input("Enter first num -> "))
            b = int(input("Enter second num -> "))
            return a*b
        case "/":
            a = int(input("Enter first num -> "))
            b = int(input("Enter second num -> "))
            return a/b
        case _:
            raise Exception("Invalid operator!")

operator = input("Please select: \n+\n-\n*\n/\n-> ")
print(calculator(operator))