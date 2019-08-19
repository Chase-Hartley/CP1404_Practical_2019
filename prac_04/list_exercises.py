
def main():

    numbers = []

    for i in range(1, 6):
        user_number = int(input("Please enter number {}/5: ".format(i)))
        numbers.append(user_number)

    print(numbers)

    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average of the numbers is: {}".format((sum(numbers) / len(numbers))))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input("Please enter your username: ")

    if user_name in usernames:
        print("Access Granted")
    else:
        print("access denied")


main()
