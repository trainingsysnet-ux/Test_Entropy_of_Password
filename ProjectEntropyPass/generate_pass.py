import random
import string


def generator(length):
    alphabet = [i for i in string.ascii_letters + string.digits + string.punctuation]
    password = ''.join(random.choices(alphabet, k=length))
    return password

