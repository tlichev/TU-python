import math


def find_square_root():
    try:
        number = int(input())
        if number > 0:
            res = math.sqrt(number)
            print(res)
        else:

            print("Invalid Number")

    except ValueError:
        print("Invalid Number")
    finally:
        print("Good Bye")



find_square_root()
