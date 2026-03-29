def average_ratios(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    total = 0
    for num in numbers:
        if num == 0:
            raise ValueError("Division by zero: cannot divide by zero")
        total += 100 / num
    return total / len(numbers)

print(average_ratios([10, 5, 0]))
