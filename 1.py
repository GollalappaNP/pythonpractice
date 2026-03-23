def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage
if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
       
       