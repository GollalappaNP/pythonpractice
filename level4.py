#take a character and check itf it is a alphabet, digit or special character
char = input("Enter the character: ")
if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:    print("The character is a special character.")


#take a number and check if it is a multiple of 3,5 or both. If it is a multiple of 3, print "Fizz". If it is a multiple of 5, print "Buzz". If it is a multiple of both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.
a = int(input("enter a number:"))
if a %3 == 0:
    print("Fizz")
elif a %5 == 0:
    print("Buzz")
elif a %3 == 0 and a %5 == 0:
    print("FizzBuzz")
else:    print(a)

#print median of three numbers
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
numbers = [a, b, c]
numbers.sort()
median = numbers[1]
print("The median of the three numbers is:", median)

#take a time in 24-hour format and determine if it is AM or PM
time = int(input("Enter the time in 24-hour format (0-23): "))
if 0 <= time < 12:
    print("its AM")
elif 12 <= time < 24:
    print("its PM")
else:    print("Invalid time entered. Please enter a number between 0 and 23.")