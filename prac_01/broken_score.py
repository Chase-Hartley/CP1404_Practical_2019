"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while not 0 <= score <= 100:
    score = (float(input("Score must be between 0 and 100. Please try again: ")))

if score >= 90:
    print("Excellent")
elif score >= 50 < 90:
    print("Passable")
else:
    print("Bad")

# TODO: Fix this!
"""Bad code"""
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")