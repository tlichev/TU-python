from area import rhombus,rectangle,square,trapezum,triangle

type = input("Please enter: \n1: Square \n2: Rectangle \n3: Triangle \n4: Trapezum \n5: Rhombus \n->").lower()

match type:
    case "square":
        print(square.square_area())
    case "rectangle":
        print(rhombus.rectangle_area())
    case "triangle":
        print(triangle.triangle_area())
    case "trapezum":
        print(trapezum.trapezum_area())
    case "rhombus":
        print(rhombus.rhombus_area())
    case _:
        print("Invalid Figure")

