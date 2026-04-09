import random
suits = {
    "♠️" : 1,
    "♥️" : 2,
    "♣️" : 3,
    "♦️" : 4,
}
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "Ace"]
special_ranks = {
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "Ace" : 14
}
deck = []

for rank in ranks:
    for suit in suits:
        deck.append([rank, suit])
random.shuffle(deck)
print(deck)
card_size = 3
hand = []
bot_hand = []
discard_pile = []

order = 0

for order in range(card_size):
    order = 0
    hand.append(deck[order]) #add a card to the player and remove the respective card from the deck
    deck.remove(deck[order])
    bot_hand.append(deck[order]) #same here, just with the bot
    deck.remove(deck[order])
print("Your hand: ", hand)
print(bot_hand)

#Placing the card:
first = random.randint(1, 2)
if first == 1:
    print("YOU START FIRST") #Placing the hand
    while True:
        try:
            choice = int(input("Press 1, 2 or 3 for the index of the card you hold: "))
            if choice > 3 or choice < 1:
                print("Invalid choice")
                continue
        except ValueError:
            print("Please enter either 1, 2, or 3.")
            continue

        discard_pile.append(hand[choice - 1])
        hand.remove(hand[choice - 1])
        hand.append(deck[order])
        deck.remove(deck[order])
        print(discard_pile)
        print(hand)
        print(len(deck))
        break
    #Bot's turn:
    

else:
    print("DEALER BEGINS FIRST")