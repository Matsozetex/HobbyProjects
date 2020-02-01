import random

"""

Syntax:

Spaces between each arg:

x d y: Roll a die with y faces x times.
dh z: Drop the highest z dice.
dl z: Drop the lowest z dice.
+ a: Add a to the total.
- b: Subtract b from the total.

"""

def getInput():
    raw = input("Enter Roll!")
    post = raw.split(" ")
    print(post)
    return post

def roller(count, face):
    j = 1
    retVal = []
    while j <= count:
        retVal.append(random.randint(1,face))
        j = j + 1
    return retVal   

def total(vals):
    i = 0
    tot = 0
    while i in range(0, len(vals)):
        tot = tot + vals[i]
        i = i + 1
    return tot


def parser(text):
    times = int(text[0])
    rolls = []
    mod = 0
    i = 1
    while i in range(1, len(text)):
        if (text[i] == 'd'):
           rolls = roller(times, int(text[i+1]))
        elif(text[i] == 'dl'):
           rolls.sort(reverse = True) 
           k = int(text[i+1])
           while k > 0:
                rolls.pop(len(rolls)-1)
                k = k - 1
        elif(text[i] == 'dh'):
           rolls.sort() 
           k = int(text[i+1])
           while k > 0:
                rolls.pop(len(rolls)-1)
                k = k - 1
        elif(text[i] == '+'):
            mod = int(text[i+1])
        elif(text[i] == '-'):
            mod = -(int(text[i+1]))
        i = i + 2
    result = total(rolls) + mod 
    print(result, rolls, mod)
parser(getInput())