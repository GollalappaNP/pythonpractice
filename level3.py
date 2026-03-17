a = int(input("enter a numer(100-999):"))
if 100 <= a <= 999:
    digits = [int(d) for d in str(a)]
    if len(set(digits)) == 3:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")
else:
    print("Number is not a 3-digit number.")