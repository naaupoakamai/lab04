def trapezoid_area(base1, base2, height):
    return ((base1+base2)*height)/2

base1=int(input("Base, first value:"))
base2=int(input("Base, second value:"))
height=int(input("Height:"))
print(f"Expected Output:{trapezoid_area(base1,base2,height)}")