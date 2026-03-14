
# This program checks if three given sides can form a valid triangle.
def is_valid_triangle(a, b, c):
    # Check if the sum of any two sides is greater than the third side
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

# Input three sides
side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

# Check if the sides form a valid triangle
if is_valid_triangle(side1, side2, side3):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")

#if valid traingle, determine the type of triangle (equilateral, isosceles, or scalene)
if is_valid_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")

#take marks 0-100 and determine the grade (A, B, C, D, F)
marks = float(input("Enter the marks (0-100): "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")   
elif marks >= 60:
    print("Grade: D")
else:    print("Grade: F")


#check if one of the two given number is a multiple of the other
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}.")
elif num2 % num1 == 0: 
    print(f"{num2} is a multiple of {num1}.")
else:    print("Neither number is a multiple of the other.")