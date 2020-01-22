import random

def newTable():
    table = []
    for i in range(9):
        table.append('')
    return table

def drawTable(table):
    print('\n%s   |  %s  |  %s' % (table[0], table[1], table[2]))
    print('---+----+---')
    print('%s   |  %s  |  %s' % (table[3], table[4], table[5]))
    print('---+----+---')
    print('%s   |  %s  |  %s' % (table[6], table[7], table[8]))
    print('\nThe following is the layout for the table: \n')
    print('1  |  2 |  3')
    print('---+----+---')
    print('4  |  5 |  6' )
    print('---+----+---')
    print('7  |  8 |  9' )

def checkAndPlace(spot, table, letter):
    retval = False
    aP = int(spot) - 1
    if(aP >= 0 and aP <= 8):
        if table[aP] in ['X', 'O']:
            return False
        else:
            table[aP]=letter
            return True
            
def winCheck(table, player):
    return ((table[0] == player and table[1]== player and table[2]==player) or
    (table[3] == player and table[4]== player and table[5]==player) or
    (table[6] == player and table[7]== player and table[8]==player) or
    (table[0] == player and table[3]== player and table[6]==player) or
    (table[1] == player and table[4]== player and table[7]==player) or
    (table[2] == player and table[5]== player and table[8]==player) or
    (table[0] == player and table[4]== player and table[8]==player) or
    (table[2] == player and table[4]== player and table[6]==player))

def aiPick(table, let):
    choice = False
    spot = random.randint(0,8)
    while choice == False:
        choice = checkAndPlace(spot, table, 'X')

def onePlayer():
    i=0
    currTable = newTable()
    player = ''
    while True:
        if(i == 9):
            print("\nIt is a draw.\n")
            break  
        drawTable(currTable)
        conPlace = False
        if(i % 2 == 0):
            player = 'O'
            while conPlace == False:
                spot = input('\nEnter a cell player %s. \n' % (player))
                conPlace = checkAndPlace(spot, currTable, player)
                if(conPlace == False):
                    print("\nInvalid entry, occupied spaces cannot be chosen. Also cells range from numbers 1-9 (inclusive)!\n")
        else:
            player = 'X'
            while conPlace == False:
                conPlace = aiPick(currTable, 'X')
        if(winCheck(currTable, player) == True):
            print('\nPlayer %s has won!' % (player))
            break
        i=i+1

def twoPlayer():
    i=0
    player = ' '
    currTable = newTable()
    while True:
        if(i == 9):
            print("\nIt is a draw.\n")
            break
        if(i % 2 == 0):
            player = 'O'
        else:
            player = 'X'
        drawTable(currTable)  
        conPlace = False
        while conPlace == False:
            spot = input('\nEnter a cell player %s. \n' % (player))
            conPlace = checkAndPlace(spot, currTable, player)
            if(conPlace == False):
                print("\nInvalid entry, occupied spaces cannot be chosen. Also cells range from numbers 1-9 (inclusive)!\n")      
        if(winCheck(currTable, player) == True):
            print('\nPlayer %s has won!' % (player))
            break
        i=i+1

def initGame():
    game = False
    while game == False:
        sel = input("\nPress 1 to play single player, press 2 to play two player.\n")
        if(sel == '1'):
            onePlayer()
            game = True
        elif(sel == '2'):
            twoPlayer()
            game = True
        else:
            print("\nInvalid input\n")

initGame()
