
numbers = [3, 1, 4, 1, 5, 9, 2]

""" What values do the following expressions have?
numbers[0] = 3
numbers [-1] = 2
numbers [3] =  1
numbers [:-1] = 3, 1 ,4 , 1 ,5 ,9
numbers [3:4] = 1
5 in numbers = true
7 in numbers = false
"3" in numbers = false
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = 10
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:7])

if 9 in numbers:
    print("true")
else:
    print("False")


