def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth number."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
if __name__ == "__main__":
    num = int(input("Enter the number of terms: "))
    print(f"Fibonacci sequence: {fibonacci(num)}")