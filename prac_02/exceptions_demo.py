"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Will occur if the user does not input a valid integer
2. When will a ZeroDivisionError occur?
Will occur if the user inputs 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Unsure
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

