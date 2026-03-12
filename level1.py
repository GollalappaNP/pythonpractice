#take a number as input and check if it is positive, negative or zero
x = float(input("Enter a number: "))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print(zero)


#check if a number is even or odd
x = float(input("Enter a number: "))
if x%2 == 0:
    print("Even")
else:    print("Odd")


#check if a number is a multiple of 5
x = float(input("Enter a number: "))
if x%5 == 0:
    print("its a multiple of 5")
else:    print("its not a multiple of 5")


#check if a number is divisible by both 3 and 5
x = float(input("Enter a number: "))
if x%3 == 0 and x%5 == 0:
    print("its divisible by both 3 and 5")     


#check if a given year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:    print(year, "is not a leap year") 


#take two numbers and the print larger number
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
if x > y:
    print(x)
else:
    print(y)


#take three numbers and print the largest number
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = float(input("Enter a third number: "))
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:    print(z)

#take a temperature value and print if it is hot, warm or cold
temp = float(input("Enter the temperature: "))
if temp > 30:
    print("Hot")
elif temp > 20:
    print("Warm")
else:    print("Cold")


#take a character as input and check if it is a vowel or consonant
x = char(input("Enter a character: "))
if x in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:    print("Consonant")