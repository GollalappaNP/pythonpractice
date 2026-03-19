#take a character and check itf it is a alphabet, digit or special character
char = input("Enter the character: ")
if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:    print("The character is a special character.")


#take a number 
a = int(input("enter a number:"))
if a %3 == 0:
    print("Fizz")
elif a %5 == 0:
    print("Buzz")
elif a %3 == 0 and a %5 == 0:
    print("FizzBuzz")
else:    print(a)