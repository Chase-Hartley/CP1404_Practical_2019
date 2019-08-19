for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars_amount = int(input("Please enter the amount of stars: "))
for i in range(stars_amount):
    print('*', end=' ')

for i in range(0, stars_amount + 1):
    print('*' * i)
