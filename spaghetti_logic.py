# Constants
ADJUSTMENT_FACTOR = 1.15

# Function to adjust a single value
def adjust_value(value: float) -> float:
    """Adjust the value by multiplying with the adjustment factor."""
    return value * ADJUSTMENT_FACTOR

# Function to format the total string
def format_total(total: float) -> str:
    """Format the total value as a string."""
    return f"Total: {total:.2f}"

# Function to log results to a file
def log_results(results: list[float]) -> None:
    """Log the results to log.txt."""
    with open("log.txt", "a") as file:
        file.write(str(results) + "\n")

# Main function to process data
def process_data(data: list[float]) -> list[float]:
    """Process the data by adjusting values, printing totals, logging, and returning results."""
    adjusted_values = [adjust_value(item) for item in data]

    for adjusted_value in adjusted_values:
        print(format_total(adjusted_value))

    log_results(adjusted_values)

    return adjusted_values
