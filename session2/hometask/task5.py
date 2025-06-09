
a = float(input("Please enter the length of side 1: "))
b = float(input("Please enter the length of side 2: "))
c = float(input("Please enter the length of side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a triangle")