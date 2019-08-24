import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    amount_of_picks = int(input("How many quick picks would you like? "))
    while amount_of_picks < 0:
        print("Value can't be less than 0 try again: ")
        amount_of_picks = int(input("How many quick picks would you like? "))

    for i in range(amount_of_picks):
        numbers = []
        for j in range(NUMBERS_PER_LINE):
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while random_number in numbers:
                random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(random_number)
            numbers.sort()
        print(" ".join("{:2}".format(random_number) for random_number in numbers))


main()


# amount_of_picks = int(input("How many quick picks would you like? "))
#
# for i in range(amount_of_picks):
#     for i in range(1, 7):
#         random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
#         NUMBERS.append(random_number)
#     print(NUMBERS.sort)
#     NUMBERS.clear()
