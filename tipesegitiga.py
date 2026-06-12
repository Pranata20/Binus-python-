def check_triangle(a, b, c):
  
    a, b, c = sorted([a, b, c])


    if a + b <= c:
        return "Not a Triangle"
    if a == b == c:
        return "Equilateral Triangle"

    is_right = abs((a**2 + b**2) - c**2) < 1e-9

    if a == b or b == c:
        if is_right:
            return "Isosceles Right-angled Triangle"
        return "Isosceles Triangle"

    if is_right:
        return "Scalene Right-angled Triangle"
    return "Scalene Triangle"


print("Enter the lengths of the three sides:")
try:
    side_a = float(input("Side A: "))
    side_b = float(input("Side B: "))
    side_c = float(input("Side C: "))

    # PROCESS & OUTPUT
    result = check_triangle(side_a, side_b, side_c)
    print(f"OUTPUT: {result}")

except ValueError:
    print("Please enter valid numerical values for the sides.")