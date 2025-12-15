import random
from modules import ints

def neiron(name=None): #Neiron Function
    lists = [random.randint(1, 100) for _ in range(50)]
    item = 1
    items = len(lists)
    count = random.randint(item, items)
    result = random.sample(lists, count)
    result2 = ints(result)
    result3 = bin(result2)
    result3 = result3[2:]
    if not name == None:
        print(name)
        print(result3)

    return result3
    #print(f"1: {result}\n2:{result2}\n3:{result3}\n4:{result4}")

def neifon(name=None): #Neifon Function
    lists = [random.randint(1, 50) for _ in range(100)]
    item = 1
    items = len(lists)
    count = random.randint(item, items)
    result = random.sample(lists, count)
    result2 = ints(result)
    result3 = bin(result2)
    result3 = result3[2:]
    if not name == None:
        print(name)
        print(result3)

    return result3

