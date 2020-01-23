import random 

def rollCheck (roun, score, player):
    flag = 0
    while flag == 0:
        roll = 0
        command = input("Player %s. Enter 'h' to hold or 'r' to roll!\n" % (player))
        if(command == 'h'):
            score = score + roun
            flag = 1
            print("\nPlayer %s. Your score is %d.\n" % (player, score))
            roun = 0
            return False
        elif(command == 'r'):
            roll = random.randint(1,6)
            print("\nYou rolled a %d.\n" % (roll))
            roun = roll + roun
            print("\nYour total is for the round is %d.\n" % (roun))
        if(roll == 1):
            roun = 0
            print("\nPlayer %s. You rolled a 1, all points lost for this round!\n" % (player))
            flag = 1
            return False
        if(roun + score >= 100):
            print("Player %s wins!\n" % (player))
            flag = 1
            return True

i = 0
win = False
p1Score = 0
p1Round = 0
p2Score = 0
p2Round = 0

while win == False:
    flag = 0
    if(i % 2 == 0):
        win = rollCheck(p1Round, p1Score, '1')
    else:
        win = rollCheck(p2Round, p2Score, '2')
    i = i + 1
        