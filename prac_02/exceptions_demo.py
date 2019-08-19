"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- If anything other than a number is added you will envoke the ValueError function
2. When will a ZeroDivisionError occur?
- If the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- You could add a while loop to keep asking for the denominator if the user inputs 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator cannot be 0, try again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
