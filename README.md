# Calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910.
## What it will do
Add, subtract, multiply and divide two numbers; display the result.
## How to run it
Run: python3 calculator.py
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.
## Alternative run command and test
Run: ./run.sh
Operate as above
Function can be tested using 6 * 7 = 42.0
## How to stop the program
Stop: ctrl + c
## Testing
File: test_calculator.py
Run: ./check.sh
7 tests & expected results:
  test_add(2, 3) == 5
  test_subtract(9, 7) == 2
  test_multiply(3, 8) == 24
  test_divide(6, 2) == 3
  test_negative_add(-6, -1) == -7
  test_negative_multiply(-5, 3) == -15
  test_uneven_divide(5, 2) == 2.5
Testing environment: source /opt/python-venv/sccm-4910/bin/activate
Exit status: 0 == All tests passed, 1 == A test failed, 5 == no tests collected
