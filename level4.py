#take a character and check itf it is a alphabet, digit or special character
char = input("Enter the character: ")
if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:    print("The character is a special character.")
