
MINIMUM_LENGTH = 5
password = input("Please enter a password (The password must be longer than {} characters): ".format(MINIMUM_LENGTH))

while len(password) < MINIMUM_LENGTH:
    print("Password does not meet the minimum length requirment of {} characters".format(MINIMUM_LENGTH))
    password = input("Please enter the password again: ")

for i in range(len(password)):
    print("*", end='')

