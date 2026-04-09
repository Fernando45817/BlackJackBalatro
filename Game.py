
ranks= [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = {
    1: "Spades", 2: "Hearts", 3: "Clubs", 4: "Diamonds"
}
ranks_special = {
    14: "A", 11: "J", 12: "Q", 13: "K"
} # Ace will also be 1 in some cases.

deck = []
print(ranks)
print(suits)

for i in range(len(ranks)*4):



