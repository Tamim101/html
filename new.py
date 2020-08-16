import string
import random

# digits

LETTERS = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation
# latter print

print(LETTERS)
print(NUMBER)
print(PUNCTUATION)


# define complier
def get_password():
    # password input
    length = input("How long do you want your password")
    return int(length)


# random password gnarator
def password_generator(length=8):
    printable = f'{LETTERS}{NUMBER}{PUNCTUATION}'
    random.shuffle(printable)

    random_password = random.choice(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


# genarator


def password_generator(length=8):
    password_one = password_generator()
    # testing password
    password_length = get_password()
    password_two = password_generator(password_length)

    print("password one(" + str(len(password_one)) + "):\t\t" + password_one)
    print("password one(" + str(len(password_two)) + "):\t\t" + password_two)


a = input("Enter a password")

