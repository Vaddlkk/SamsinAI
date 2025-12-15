import random

def ints(numbers):
    adstring = "".join(map(str, numbers))
    digitsl = list(adstring)
    random.shuffle(digitsl)
    sstring = "".join(digitsl)
    number = int(sstring)
    return number
