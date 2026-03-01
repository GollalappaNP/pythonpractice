def is_palindrome(sequence):
    # Convert the sequence to a string and normalize case
    sequence = str(sequence).lower()
    # Check if the sequence is equal to its reverse
    return sequence == sequence[::-1]

# Example usage
if __name__ == "__main__":
    test_sequence = input("Enter a sequence to check if it's a palindrome: ")
    if is_palindrome(test_sequence):
        print("The sequence is a palindrome!")
    else:
        print("The sequence is not a palindrome.")