from math import tan,pi

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * tan(pi / n))

n = int(input("Input number of sides:"))
s = int(input("Input the length of a side:"))


area = regular_polygon_area(n, s)
print(f"The area of the polygon is:{area:.2f}")
