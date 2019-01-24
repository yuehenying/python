from random import randint

def randomNumber(num):
    result = ""
    for i in range(0,num):
        j = randint(0,9)
        result += str(j)
    return int(result)