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
		Dtotal = 11
		print("Dealer did not have a BlackJack \n You are safe for now")
else:
	Dtotal = DealerHand[0]


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
print("Dealer: ", DealerHand[0], "??")

#Player decisions:
Win = False
Lose = False

decisions = ["stand", "hit", "double down", "split" ]

if Ptotal != 21:
	if PlayerHand[0] != PlayerHand[1]:
		choiceSH = int(input("Press 0 to stand\nPress 1 to hit"))
		print(decisions[choiceSH])
		#if choiceSH == 0:
			#Dealer will check his cards and then hit or stand(I'll do it later)
		#elif choiceSH == 1:
			#The player will get another card(I'll do later)
		#else:
			#print("Choose actual options")



	print("Make a decision")
else:
	print("You win")









#Dtotal = sum(DealerHand)
#print("Player:", PlayerHand, "Total: ", Ptotal)
#print("Dealer: ", DealerHand[0], "??")