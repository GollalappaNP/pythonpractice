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


