import calendar

def print_square(number):
    square = number ** 2
    print(f"The square of {number} is {square}")

# Example usage
num = int(input("Enter a number: "))
print_square(num)


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(calendar.month(year, month))


# Swapping two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap logic
a, b = b, a

print(f"After swapping: first number = {a}, second number = {b}")


# Finding LCM of two numbers
def find_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter the first number to find LCM: "))
num2 = int(input("Enter the second number to find LCM: "))

lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}")