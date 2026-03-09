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

# Factorial of a number
def factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif number == 0 or number == 1:
        return 1
    else:
        fact = 1
        for i in range(2, number + 1):
            fact *= i
        return fact

# Example usage
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
if result is not None:
    print(f"The factorial of {num} is {result}")

    # Sum of digits of a number
    def sum_of_digits(number):
        if number < 0:
            number = -number  # Handle negative numbers
        return sum(int(digit) for digit in str(number))

    # Example usage
    num = int(input("Enter a number to find the sum of its digits: "))
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is {result}")

    # Bubble Sort
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Example usage
    numbers = list(map(int, input("Enter a list of numbers to sort using Bubble Sort, separated by spaces: ").split()))
    bubble_sort(numbers)
    print(f"Sorted list: {numbers}")

    
    
if 3 in s:
        print("3 is in the set")
    else:
        print("3 is not in the set")

        # Merge Sort
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0

                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        # Example usage
        numbers = list(map(int, input("Enter a list of numbers to sort using Merge Sort, separated by spaces: ").split()))
        merge_sort(numbers)
        print(f"Sorted list: {numbers}")