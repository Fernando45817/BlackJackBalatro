import random

numdecks = 6
suits = 4
cards =numdecks * suits
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = []



for i in range(cards):
	for i in range(len(ranks)):
			deck.append(ranks[i])
random.shuffle(deck)
print(deck)	#remove this later, it is just to know my deck

#first shuffle and deal:

PlayerHand = []
DealerHand = []


for c in range(2):
	PlayerHand.append(deck[c+c])
	DealerHand.append(deck[(c+1)+c])

#Econ stuff:
money_process = False
withdrawal = int(input("Cash in your money"))
balance = withdrawal

while not money_process:
	bets = int(input("Bet some of your balance"))
	if bets > balance :
		print("You don't have enough funds")
	elif bets < 0:
		print("Bet actual money, dumbass")
	else:
		print("Money bet: ", bets)
		money_process = True

#Dealer's amount or Aces:
if "A" in DealerHand:
	if DealerHand.index("A") == 0 and 10 in DealerHand:
		Dtotal = 21
		print("Dealer wins")
	elif DealerHand.index("A") == 0 and not 10 in DealerHand:
		Dsubtotal = 11
		Dtotal = Dsubtotal + DealerHand[1]
		print("Dealer did not have a BlackJack \n You are safe for now")
else:
	Dsubtotal = DealerHand[0]
	Dtotal = sum(DealerHand)


#Player's amount:
if "A" in PlayerHand:
	if PlayerHand.index("A") == 0 and PlayerHand.index("A") == 1:
		Ptotal = 12
	#elif PlayerHand.index("A") == 0 and PlayerHand.index(10) == 1 or PlayerHand.index(10) == 0 and PlayerHand.index("A") == 1:
	elif "A" and 10 in PlayerHand:
		Ptotal = 21

	elif "A" and not 10 in PlayerHand:
		indexA = PlayerHand.index("A")
		if indexA == 0:
			Ptotal = 11 + PlayerHand[1]
		else:
			Ptotal = 11 + PlayerHand[0]

else:
	Ptotal = sum(PlayerHand)

print("Player: ", PlayerHand, "Total: ", Ptotal)
print("Dealer: ", DealerHand[0], "??", Dsubtotal)

#Player decisions:
Win = False
Lose = False

decisions = ["stand", "hit", "double down", "split" ]
choiceSH = ["stand", "hit"]

if PlayerHand[0] == PlayerHand[1]:
	SorH = int(input("Press 0 to stand, 1 to hit, 2 to double down, 3 to split: "))
	if SorH == 0:
		#Dealer will continue their actions
		while sum(DealerHand) < 17:
			DealerHand.append(deck[(c + 2) + c])
		print(DealerHand)

#else:
	#SorH = int(input("Press 0 to stand, 1 to hit, 2 to double down: "))
	#if SorH










#Dtotal = sum(DealerHand)
#print("Player:", PlayerHand, "Total: ", Ptotal)
#print("Dealer: ", DealerHand[0], "??")