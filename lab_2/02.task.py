import math

r = float(input("Please enter a radius r -> "))

perimeter = 2*math.pi*r

area = math.pi*(r**2)

print("-"*20)
print(f"Perimeter is {perimeter:.3f}")
print("-"*20)
print(f"Area is {area:.3f}")
print("-"*20)
