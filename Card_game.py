import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♣', '♥', '♦']
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

def shuffle_and_distribute(deck, num_players):
    random.shuffle(deck)
    players = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        players[i % num_players].append(card)
    return players


deck = create_deck()
players = shuffle_and_distribute(deck, 2)
player1, player2 = players

print("Player 1's cards:", player1)
print("Player 2's cards:", player2)

