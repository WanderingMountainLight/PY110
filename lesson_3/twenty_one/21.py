# intial_deck =[
#     {'rank': 'Ace', 'suit': 'Spades'},
#     {'rank': 2, 'suit': 'Spades'},
#     {'rank': 3, 'suit': 'Spades'},
#     {'rank': 4, 'suit': 'Spades'},
#     {'rank': 5, 'suit': 'Spades'},
#     {'rank': 6, 'suit': 'Spades'},
#     {'rank': 7, 'suit': 'Spades'},
#     {'rank': 8, 'suit': 'Spades'},
#     {'rank': 9, 'suit': 'Spades'},
#     {'rank': 10, 'suit': 'Spades'},
#     {'rank': 'Jack', 'suit': 'Spades'},
#     {'rank': 'Queen', 'suit': 'Spades'},
#     {'rank': 'King', 'suit': 'Spades'},
#     {'rank': 'Ace', 'suit': 'Hearts'},
#     {'rank': 2, 'suit': 'Hearts'},
#     {'rank': 3, 'suit': 'Hearts'},
#     {'rank': 4, 'suit': 'Hearts'},
#     {'rank': 5, 'suit': 'Hearts'},
#     {'rank': 6, 'suit': 'Hearts'},
#     {'rank': 7, 'suit': 'Hearts'},
#     {'rank': 8, 'suit': 'Hearts'},
#     {'rank': 9, 'suit': 'Hearts'},
#     {'rank': 10, 'suit': 'Hearts'},
#     {'rank': 'Jack', 'suit': 'Hearts'},
#     {'rank': 'Queen', 'suit': 'Hearts'},
#     {'rank': 'King', 'suit': 'Hearts'},
#     {'rank': 'Ace', 'suit': 'Clubs'},
#     {'rank': 2, 'suit': 'Clubs'},
#     {'rank': 3, 'suit': 'Clubs'},
#     {'rank': 4, 'suit': 'Clubs'},
#     {'rank': 5, 'suit': 'Clubs'},
#     {'rank': 6, 'suit': 'Clubs'},
#     {'rank': 7, 'suit': 'Clubs'},
#     {'rank': 8, 'suit': 'Clubs'},
#     {'rank': 9, 'suit': 'Clubs'},
#     {'rank': 10, 'suit': 'Clubs'},
#     {'rank': 'Jack', 'suit': 'Clubs'},
#     {'rank': 'Queen', 'suit': 'Clubs'},
#     {'rank': 'King', 'suit': 'Clubs'},
#     {'rank': 'Ace', 'suit': 'Diamonds'},
#     {'rank': 2, 'suit': 'Diamonds'},
#     {'rank': 3, 'suit': 'Diamonds'},
#     {'rank': 4, 'suit': 'Diamonds'},
#     {'rank': 5, 'suit': 'Diamonds'},
#     {'rank': 6, 'suit': 'Diamonds'},
#     {'rank': 7, 'suit': 'Diamonds'},
#     {'rank': 8, 'suit': 'Diamonds'},
#     {'rank': 9, 'suit': 'Diamonds'},
#     {'rank': 10, 'suit': 'Diamonds'},
#     {'rank': 'Jack', 'suit': 'Diamonds'},
#     {'rank': 'Queen', 'suit': 'Diamonds'},
#     {'rank': 'King', 'suit': 'Diamonds'}
# ]
import random

def build_deck():
    deck = []
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    for suit in suits:
        for value in ranks:
            deck.append({'rank': value, 'suit': suit})
    return deck


# for item in initial_deck:
#     print(item)

def shuffle(deck):
   random.shuffle(deck)


# for item in initial_deck:
#     print(item)

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def cal_total(hand):
    total = 0
    for card in hand:
        if card['rank'] == 'Ace':
            total += 11
        elif card['rank'] in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            total += card['rank']
    return total


def is_busted(total):
    return total > 21

def ace_value(score, hand):
    aces = len([card['rank'] for card in hand if card['rank'] == 'Ace'])
    while score > 21 and aces >= 1:
            score -= 10
            aces -= 1
    return score

player_hand = []
dealer_hand = []

initial_deck = build_deck()

shuffle(initial_deck)

deal_card(initial_deck, player_hand)
deal_card(initial_deck, player_hand)

deal_card(initial_deck, dealer_hand)
deal_card(initial_deck, dealer_hand)

print(f'Player has {player_hand}')
# print(f'Dealer has {dealer_hand}')

player_score = cal_total(player_hand)

is_busted(player_score)
ace_value(player_score, player_hand)