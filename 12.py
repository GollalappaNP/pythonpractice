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


# FLAMES game
def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1 + name2)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()

    return flames[0]

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")


# Check if a number is positive, negative, or zero
def check_number_sign(number):
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is zero.")

# Example usage
num = int(input("Enter a number to check if it's positive, negative, or zero: "))
check_number_sign(num)

# Check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

# Example usage
num = int(input("Enter a number to check if it's even or odd: "))
check_even_odd(num)



# Find the largest number in a list
def find_largest_in_list(numbers):
    if not numbers:
        print("The list is empty.")
        return None
    largest = max(numbers)
    print(f"The largest number in the list is {largest}")

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
find_largest_in_list(numbers)

# Check if a character is a vowel or consonant
def check_vowel_consonant(char):
    vowels = "aeiouAEIOU"
    if len(char) == 1 and char.isalpha():
        if char in vowels:
            print(f"The character '{char}' is a vowel.")
        else:
            print(f"The character '{char}' is a consonant.")
    else:
        print("Please enter a single alphabetic character.")

# Example usage
char = input("Enter a character to check if it's a vowel or consonant: ")
check_vowel_consonant(char)



#chocolate problem

def push_zero_to_end(arr):
    non_zero = [num for num in arr if num != 0]
    zero_count = len(arr) - len(non_zero)
    result = non_zero + [0] * zero_count
    return result

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
result = push_zero_to_end(numbers)
print(f"List after pushing zeros to the end: {result}")

