# Calculator with File Storage

## Overview
This is a simple Python-based calculator that performs basic arithmetic operations and stores the calculations in a text file (`calculations.txt`).

## Features
- Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
- Prevents division by zero errors
- Saves each calculation to a file
- Displays previously stored calculations

## Installation
Ensure you have Python installed on your system.

1. Clone this repository:
   ```sh
   git clone <https://github.com/yukti-says/calculator_with_data_save>
   ```

## Usage
Run the script using Python:
```sh
 main.py
```
Follow the prompts to enter numbers and an operation. The result will be displayed and stored in `calculations.txt`.

## Example
```
Choose an operation: +, -, *, /
Enter operator: +
Enter first number: 10
Enter second number: 5
Result: 15.0

Stored Calculations:
10 + 5 = 15.0
```

## File Handling
- The script appends new calculations to `calculations.txt`
- If the file exists, previous calculations are preserved and displayed upon running the script

## License
This project is open-source. Feel free to modify and share.
