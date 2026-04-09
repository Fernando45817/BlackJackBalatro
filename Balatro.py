
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
hand_size = 8
for rank in ranks:
    for suit in suits:
        deck.append([rank, suit])
random.shuffle(deck)
print(deck)
hand = []
for order in range(hand_size):
    hand.append(deck[order])
print(hand)

#Hand levels:

multReg = 0
chipsReg = 0
hchips = 5 #high card
hmult = 1
pchips = 10 #pair
pmult = 2
tpchips = 20 #two pair
tpmult = 2
toakchips = 30 #three of a kind
toakmult = 3
strchips = 30 #straight
strmult = 4
flchips = 35 #flush
flmult = 4
fhchips = 40 #full house
fhmult = 4
foakchips = 60 #four of a kind
foakmult = 7
strflchips = 100 #straight flush
strflmult = 8
FOAKchips = 120 #Five of a kind
FOAKmult = 12
FLHchips = 140 #Flush house
FLHmult = 14
FL5chips = 160 #Flush five
FL5mult = 16



High_card = (chipsReg + hchips) * (multReg + hmult)
Pair = (chipsReg + pchips) * (multReg + pmult)
Two_Pair = (chipsReg + tpchips) * (multReg + tpmult)
toaK = (chipsReg + toakchips) * (multReg + toakmult)
Straight = (chipsReg + strchips) * (multReg + strmult)
Flush = (chipsReg + flchips) * (multReg + flmult)
Full_house = (chipsReg + fhchips) * (multReg + fhmult)
foaK =(chipsReg + foakchips) * (multReg + foakmult)
Straight_flush = (chipsReg + strflchips) * (multReg + strflmult)
FOAK = (chipsReg + FOAKchips) * (multReg + FOAKmult)
Flush_house = (chipsReg + FLHchips) * (multReg + FLHmult)
Flush_five = (chipsReg + FL5chips) * (multReg + FL5mult)


