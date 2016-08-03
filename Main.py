import random

cardIndex = [["Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs","5 of Clubs","6 of Spad\
es","7 of Clubs", "8 of Clubs", "9 of Clubs","10 of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs"],["Ace of Diamonds", "2 of D\
iamonds", "3 of Diamonds", "4 of Diamonds","5 of Diamonds","6 of Spad\
es","7 of Diamonds", "8 of Diamonds", "9 of Diamonds","10 of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds"],["Ac\
e of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts","5 of Hearts","6 of Spad\
es","7 of Hearts", "8 of Hearts", "9 of Hearts","10 of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts"],["Ac\
e of Spades", "2 of Spades", "3 of Spades", "4 of Spades","5 of Spades","6 of Spad\
es","7 of Spades", "8 of Spades", "9 of Spades","10 of Spades","Jack of Spades","Queen of Spades","King of Spades"]]
players = "a"
while players != "1" and players != "2" and players != "3" and players != "4":
    players = raw_input("How many players?")
    if str(players) == "4":
        print "Multiplayer currently in progress. Sorry."
        exit()
    if str(players) == "3":
        print "Multiplayer currently in progress. Sorry."
        exit()
    if str(players) == "2":
        print "Multiplayer currently in progress. Sorry."
        exit()
    if str(players) == "1":
        print
    else:
        print "Please enter valid input (1, 2, 3, or 4)."
yourCards = []
comACards = []
comBCards = []
comCCards = []
for null in range(0,13):
    yourCards.append(cardIndex[random.randint(0,3)][random.randint(0,12)])
    comACards.append(cardIndex[random.randint(0,3)][random.randint(0,12)])
    comBCards.append(cardIndex[random.randint(0,3)][random.randint(0,12)])
    comCCards.append(cardIndex[random.randint(0,3)][random.randint(0,12)])
print "Your cards: " 
print
for y in yourCards:
    print y
for null in range(0,13):
    print "Coming Soon!"
    

    



