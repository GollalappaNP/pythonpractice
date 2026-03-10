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