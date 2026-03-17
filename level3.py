
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