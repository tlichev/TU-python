RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = '\033[0m'

def figure_area(type):
    if type == "square":
        a = float(input("Enter a -> "))
        print("-"*20)
        draw_square()
        res = area_of_square(a)
        print(f"Area of square is {res:.2f}")
    if type == "rectangle":
        a = float(input("Enter a -> "))
        b = float(input("Enter b -> "))
        print("-" * 20)
        draw_rectangle()
        res = area_of_rectangle(a,b)
        print(f"Area of rectangle is {res:.2f}")
    if type == "triangle":
        a = float(input("Enter a -> "))
        b = float(input("Enter b -> "))
        print("-" * 20)
        draw_triangle()
        res = area_of_triangle(a, b)
        print(f"Area of triangle is {res:.2f}")





def area_of_square(a):
    return a*a

def area_of_rectangle(a,b):
    return a*b

def area_of_triangle(a,b):
    return (a*b)/2

def draw_square():
    x = 5;
    for i in range(x):
        print(BLUE + "*  " * x + RESET)

def draw_rectangle():
    x = 5
    y = 3
    for i in range(y):
        print(YELLOW + "*  " * x + RESET)

def draw_triangle():
    x = 5

    for i in range(x):
        print(RED + "*  " * i + RESET)


type = input("Please enter: \n1: Square \n2: Rectangle \n3: Triangle \n->").lower()


figure_area(type)