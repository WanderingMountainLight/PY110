import random

def prompt(phrase):
    print(f'===> {phrase}')

def build_deck():
    deck = []
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    for suit in suits:
        for value in ranks:
            deck.append({'rank': value, 'suit': suit})
    return deck

def shuffle(deck):
   random.shuffle(deck)

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def calc_total(hand):
    total = 0
    for card in hand:
        if card['rank'] == 'Ace':
            total += 11
        elif card['rank'] in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            total += card['rank']
    total = ace_value(total, hand)
    return total


def is_busted(total):
    return total > 21

def ace_value(score, hand):
    aces = len([card['rank'] for card in hand if card['rank'] == 'Ace'])
    while score > 21 and aces >= 1:
            score -= 10
            aces -= 1
    return score

def player_hit():
    prompt('Would you like to hit or stay?')
    while True:
        response = input().strip().lower()
        if response in ['hit', 'stay']:
            if response == 'hit':
                return True
            else:
                return False
        else:
            prompt('That is not a valid input. Please choose hit or stay')

#def dealer_logic(hand):
    #work_in_progress

def score_comparison(player, dealer):
    if player <= 21 and dealer <= 21:
        if player == dealer:
            return f"The game ends in a tie."
        elif player > dealer:
            return f'Player wins! Final score {player} - {dealer}'
        elif dealer > player:
                    return f'Dealer wins! Final score {dealer} - {player}'
    else:
        if player > 21:
            return f'Player busted. Dealer wins.'
        elif dealer > 21:
            return f'Dealer busted. Player wins'

def display_hand(hand, hide_extra_cards=False):
    card_strings = []
    for card in hand:
        card_strings.append(f"{card['rank']} of {card['suit']}")
    if hide_extra_cards:
        display = [card_strings[0], 'Unknown']
        hand_string = ', '.join(display)
        return hand_string
    else:
        hand_string = ', '.join(card_strings)
        return hand_string


def game_loop():

        player_hand = []
        dealer_hand = []

        prompt('Welcome to 21.')

        initial_deck = build_deck()

        shuffle(initial_deck)

        deal_card(initial_deck, player_hand)
        deal_card(initial_deck, player_hand)

        deal_card(initial_deck, dealer_hand)
        deal_card(initial_deck, dealer_hand)

        print(f'You currently hold: {display_hand(player_hand)}')
        print(f"The dealer currently holds: {display_hand(dealer_hand, True)}")

        player_score = calc_total(player_hand)
        dealer_score = calc_total(dealer_hand)

        print(f'Your current score is {player_score}')

        while player_hit():
            deal_card(initial_deck, player_hand)
            print(f'You currently hold: {display_hand(player_hand)}')
            player_score = calc_total(player_hand)
            if is_busted(player_score):
                break
            print(f'Your current score is {player_score}')

        if is_busted(player_score):
            score_comparison(player_score, dealer_score)
        else:


        

        # is_busted(player_score)
        # ace_value(player_score, player_hand)

game_loop()