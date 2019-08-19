"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    print(get_mark(score))


def get_mark(score):

    while not 0 <= score <= 100:
        score = (float(input("Score must be between 0 and 100. Please try again: ")))

    if score >= 90:
        score = "Excellent"
        return score
    elif score >= 50 < 90:
        score = "Passable"
        return score
    else:
        score = "Bad"
        return score


main()

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