import random

# class Card(object):
#     def __init__(self):
#         self.suits = ["S", "H", "C", "D"]
#         self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#         self.suit = None
#         self.value = None
#
#     def check_values(self):
#         if cvalue == num in range(0, 11):
#             self.value = num
#         if value == "J":
#             self.value = 10
#         if fvalue == "Q":
#             self.value = 10
#         if fvalue == "K":
#             self.value = 10
#
# aCard = Card()

class Deck(object):
    deck = []
    # function creates a full deck of 52 cards and shuffles them
    def __init__(self):
        self.suits = None
        self.values = None
        self.deck = []

    def create_deck(self):
        self.suits = ["S", "H", "C", "D"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for value in self.values:
            for suit in self.suits:
                self.deck.append(value + suit)
        random.shuffle(self.deck)
        return self.deck

class Player(object):
    def __init__(self):
        self.bust = 22
        self.hand = []

class Dealer(Player):
    def __init__(self):
        self.stand = 17
        self.bust = 22
        self.hand = []

# ended up ot using
class Blackjack(object):
    def __init__(self):
        self.blackjack_value = 21

def main():
    players = []
    player_hands = []
    dealer = Dealer()
    deck1 = Deck()
    deck1 = deck1.create_deck()

    # creates players
    num_players = input("How many players are playing?   ")
    for num in range(1, int(num_players) + 1):
        aPlayer = Player()
        players.append(aPlayer)
        player_hands.append("")

    # deals players their cards
    for deal in range(0, 2):
        dealer.hand.append(deck1.pop())
        for player in range(0, len(players)):
            players[player].hand.append(deck1.pop())

    # output
    print("Dealer hand: ", dealer.hand, "=", check_total(dealer.hand))
    for player in players:
        print("Player", players.index(player)+1, "hand: ", player.hand, "=", check_total(player.hand))
        player_hands[players.index(player)] = check_total(player.hand)

    print()

    # players hit or stay
    for player in players:
        print()

        print("Player " + str(players.index(player) + 1) + " hand:", player.hand, "=", check_total(player.hand))
        choice = "y"
        while choice == "y":
            choice = input("Player " + str(players.index(player)+1) + ", do you want to take a hit? [y/n]   ")
            if choice == "y":
                players[players.index(player)].hand.append(deck1.pop())
                print("Your new hand:   ", player.hand, "=", check_total(player.hand))
                player_hands[players.index(player)] = check_total(player.hand)

                if check_total(player.hand) >= player.bust:
                    print("You busted!")
                    print(player_hands[players.index(player)])
                    choice = "n/a"

    print()

    # dealer's hand
    print("Dealer's turn")
    print("Dealer's hand:", dealer.hand, "=", check_total(dealer.hand))
    while check_total(dealer.hand) < 17:
        dealer.hand.append(deck1.pop())
        print("Dealer's hand: ", dealer.hand, "=", check_total(dealer.hand))
    if check_total(dealer.hand) >= 17 and check_total(dealer.hand) <= 21:
        print("Dealer stays at", check_total(dealer.hand))
        print()
    if check_total(dealer.hand) >= dealer.bust:
        print("Dealer busted!")
        print()

    check_winners(check_total(dealer.hand), player_hands)

def check_total(hand):
    total = 0
    for card in hand:
        for num in range(2, 11):
            if str(card).find(str(num)) != -1:
                total += num
        if (str(card).find(str(1)) != -1) and (str(card).find(str(10)) == -1):
            total += 1
        if str(card).find("J") != -1:
            total += 10
        if str(card).find("Q") != -1:
            total += 10
        if str(card).find("K") != -1:
            total += 10
        if str(card).find("A") != -1:
            if total < 11:
                total += 11
            else:
                total += 1
    return total

def check_winners(dhand, phands):
    winners = []
    if dhand >= 22:
        for x in range(0, len(phands)):
            if phands[x] <= 21:
                winners.append("Player " + (str(x + 1)))
    else:
        for x in range(0, len(phands)):
            if phands[x] > dhand and phands[x] <= 21:
                winners.append("Player " + (str(x + 1)))
    if len(winners) == 0:
        print("Dealer wins")
    else:
        print("Winners:", winners)

    # return winners


main()