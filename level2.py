
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