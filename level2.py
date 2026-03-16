
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


#time moudule to get the current time and print it in the format HH:MM:SS
import time
current_time = time.strftime("%H:%M:%S")
print("Current time:", current_time)
if current_time >= "00:00:00" and current_time < "12:00:00":
    print("Good morning!")
elif current_time >= "12:00:00" and current_time < "18:00:00":
    print("Good afternoon!")
else:    print("Good evening!")

#check voting eligibility based on age
age = int(input("Enter your age: "))
if age > 18:
    print("eligible to vote")
else:    print("not eligible to vote")

#take two numbers and determine whether both numbers are even, odd, or one of each
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:    print("One number is even and the other is odd.")

#take an alphabet and check if it lies between a to m or n to z
alphabet = input("Enter an alphabet: ").lower()
if 'a' <= alphabet <= 'm':
    print(f"{alphabet} lies between a and m.")
elif 'n' <= alphabet <= 'z':
    print(f"{alphabet} lies between n and z.")
else:    print("Invalid input. Please enter a single alphabet.")


#take a day 1-7 and print the corresponding day of the week
day = int(input("Enter a day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:  
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday") 
else:    print("Invalid input. Please enter a number between 1 and 7.")


month = int(input("Enter a month number (1-12): "))
if month == 1, 3, 5, 7, 8, 10, 12:
    print("31 days")
elif month == 4, 6, 9, 11:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:    print("Invalid input. Please enter a number between 1 and 12.")
