import random
import string


def generator():
    l = 12
    alphabet = [i for i in string.ascii_letters + string.digits + string.punctuation]
    password = ''.join(random.choices(alphabet, k=l))
    return password
    # while True:
    #     password = ''.join(random.sample(alphabet, l))
    #     if entropy(password) >= 70:
    #         return password
    #     else:
    #         continue

    

print(generator())
