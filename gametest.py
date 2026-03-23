if Ptotal != 21:
    if PlayerHand[0] != PlayerHand[1]:
        choice1 = int(input("Press 0 to stand\nPress 1 to hit"))
        print(choiceSH[choice1])
        if choiceSH == 0:
            # Dealer will check his cards and then hit or stand(I'll do it later)
            print(DealerHand)
            if sum(DealerHand) > 16:

            while sum(DealerHand) < 17:
                print(DealerHand)
                DealerHand.append(deck[(c + 1) + c])
        elif choiceSH == 1:
            print("test")
        # The player will get another card(I'll do later)
        else:
            print("option")
        # print("Choose actual options")

    print("Make a decision")
else:
    print("You win")

    #Barebones of the process of hitting and standing

while Ptotal != 21:  #Has to be different, otherwise cycle will be repeating without bets and other shit.
	#Player will decide either to hit or stand, or have more options
	if PlayerHand[0] != PlayerHand[1]:
		choice1 = int(input("Press 0 to stand\n Press 1 to hit"))
		print(choiceSH[choice1])
		if choice1 == 0:
			print("Dealer's hand: ", DealerHand)
			while Dtotal < 17:
				DealerHand.append(deck[(c + 2) + c])
			print(DealerHand)
			if Dtotal > Ptotal:
				print("Dealer wins") #For now it can be like this, but later, the dealer will win the money of the player
			elif Dtotal == Ptotal:
				print("Tie, you get back your bets") #same here, I'll add later
			else:
				print("Player wins") #Player will get +(x1) his bet to the balance
		else:
			print("in process for now")
