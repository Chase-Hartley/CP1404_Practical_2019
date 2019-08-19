import random

for i in range(1, 10):
    print(random.randint(5, 20))
    print(random.randrange(3, 10, 2))
    print(random.uniform(2.5, 5.5))

"""
Line 1: Requires a random integer between 5 and 20, the smallest number being 5 and the largest being 20.
Line 2: Requires a random number between the range of 3  and 9 in steps of 2. Smallest 3 highest 9, possible numbers
        (3,5,7,9)
Line 3: Requires a random number by setting a lower and upper limit. Smallest being 2.5 highest being 5.5.
"""
