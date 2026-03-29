# MCP Student Sandbox

This repository is a sandbox for learning and practicing Python programming concepts, including code refactoring, bug fixing, security analysis, and documentation.

## Files Overview

### mystery_module.py
Contains a function for solving quadratic equations.

#### Function: `fn_x(a, b, c)`
Solves the quadratic equation \( ax^2 + bx + c = 0 \) using the quadratic formula.

**Parameters:**
- `a` (float): Coefficient of \( x^2 \). Must not be zero.
- `b` (float): Coefficient of \( x \).
- `c` (float): Constant term.

**Return Values:**
- If the discriminant \( d = b^2 - 4ac \) is negative, returns `None` (no real roots).
- Otherwise, returns a tuple of two floats: the roots \( \frac{-b \pm \sqrt{d}}{2a} \).

**Raises:**
- No explicit exceptions, but division by zero if `a` is zero (though not handled).

**Usage Examples:**

```python
from mystery_module import fn_x

# Example 1: Two real roots
roots = fn_x(1, -3, 2)  # x^2 - 3x + 2 = 0
print(roots)  # (2.0, 1.0)

# Example 2: One repeated root (discriminant = 0)
roots = fn_x(1, -2, 1)  # x^2 - 2x + 1 = 0
print(roots)  # (1.0, 1.0)

# Example 3: No real roots
roots = fn_x(1, 0, 1)  # x^2 + 1 = 0
print(roots)  # None
```

### failing_calculator.py
Contains a function `average_ratios` that calculates the average of 100 divided by each number in a list.

**Note:** This file has been fixed to handle division by zero and empty lists.

### secret_leak.py
Demonstrates a security vulnerability with a hardcoded AWS secret key. **Do not use in production!**

### spaghetti_logic.py
An example of poorly structured code that has been refactored into modular functions for better maintainability.

## Installation
Clone the repository:
```bash
git clone https://github.com/saidoztrk/mcp-student-sandbox.git
cd mcp-student-sandbox
```

## Requirements
- Python 3.6+

## Contributing
This is a learning repository. Feel free to submit issues or pull requests for improvements.

## License
MIT License