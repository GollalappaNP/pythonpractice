
# Write a program that takes a three-digit number as input and checks if all the digits are distinct. If they are, print "All digits are distinct." Otherwise, print "Digits are not distinct."
a = int(input("enter a numer(100-999):"))
if 100 <= a <= 999:
    digits = [int(d) for d in str(a)]
    if len(set(digits)) == 3:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")
else:
    print("Number is not a 3-digit number.")


#Take a 3 digit number and determine if the middle digit is the largest,smallest or neither of the three digits.
a = int(input("enter a numer(100-999):"))
if 100 <= a <= 999:
    digits = [int(d) for d in str(a)]
    middle_digit = digits[1]
    if middle_digit > digits[0] and middle_digit > digits[2]:
        print("The middle digit is the largest.")
    elif middle_digit < digits[0] and middle_digit < digits[2]:
        print("The middle digit is the smallest.")
    else:
        print("The middle digit is neither the largest nor the smallest.")
else:    print("Number is not a 3-digit number.")


#take  a 4 digit number and check if the first and last digits are the same. If they are, print "The first and last digits are the same." Otherwise, print "The first and last digits are different."
a = int(input("enter a numer(1000-9999):"))
if 1000 <= a <= 9999:
    digits = [int(d) for d in str(a)]
    if digits[0] == digits[3]:
        print("The first and last digits are the same.")
    else:
        print("The first and last digits are different.")
else:    print("Number is not a 4-digit number.")   

#check whether a given digit is single,double or multi digit
a = int(input("enter a numer:"))
if 0 <= a <= 9:
    print("The digit is a single digit.")
elif 10 <= a <= 99:
    print("The digit is a double digit.")
else:    print("The digit is a multi digit.")   

#check if a number is multiple of seven or ends with 7
a = int(input("enter a numer:"))
if a % 7 == 0 or str(a).endswith('7'):
    print("The number is a multiple of seven or ends with 7.")
else:    print("The number is not a multiple of seven and does not end with 7.")


#take co-ordinates (x,y) and determine the quadrant in which the point lies
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the first quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the second quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the third quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the fourth quadrant.")
else:    print("The point lies on the origin or on one of the axes.")


#check if an amount can be evenly divided into 2000,500,and 100 currnecy notes 
amount = int(input("Enter the amount: "))
if amount % 100 == 0:
    num_2000 = amount // 2000
    amount %= 2000
    num_500 = amount // 500
    amount %= 500
    num_100 = amount // 100
    print(f"The amount can be divided into {num_2000} notes of 2000, {num_500} notes of 500, and {num_100} notes of 100.")
else:    print("The amount cannot be evenly divided into 2000, 500, and 100 currency notes.")

#check if a number lies within range[100,999]
a = int(input("enter a number:"))
if 100 <= a <= 999:
    print("The number lies within the range [100, 999].")
else:    print("The number does not lie within the range [100, 999].")


#take two angles of a triangle and compute the third angle
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))
if 0 < angle1 < 180 and 0 < angle2 < 180 and angle1 + angle2 < 180:
    angle3 = 180 - (angle1 + angle2)
    print(f"The third angle of the triangle is: {angle3} degrees.")
else:    print("Invalid angles. The sum of the two angles must be less than 180 degrees, and each angle must be between 0 and 180 degrees.")


#check whether a number is perfect square or not
import math 
a = int(input("enter a number:"))
if a >= 0:
    sqrt_a = int(math.sqrt(a))
    if sqrt_a * sqrt_a == a:
        print(f"{a} is a perfect square.")
    else:
        print(f"{a} is not a perfect square.")
else:    print("Negative numbers cannot be perfect squares.")

#check whether a number is perfect square or not
import math 
a = int(input("enter a number:"))
if a >= 0:
    sqrt_a = int(math.sqrt(a))
    if sqrt_a * sqrt_a == a:
        print(f"{a} is a perfect square.")
    else:
        print(f"{a} is not a perfect square.")
else:    print("Negative numbers cannot be perfect squares.")