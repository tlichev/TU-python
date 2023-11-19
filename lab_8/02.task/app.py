from operations import substract_nums, multiply_nums, divide_nums, sum_nums
operator = input("Please select: \n+\n-\n*\n/\n-> ")

match operator:
    case "+":
        print(sum_nums.n_sum())
    case "-":
        print(substract_nums.subtract())
    case "*":
        print(multiply_nums.multiply())
    case "/":
        print(divide_nums.divide())
    case _:
        raise Exception("Invalid operator!")

