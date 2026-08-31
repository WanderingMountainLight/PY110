"""PY110 Twenty-One card game"""

import random

TARGET_SCORE = 21
CPU_HIT_LIMIT = 17
BEST_OF = 5
WINS_NEEDED = BEST_OF // 2 + 1

def prompt(phrase):
    """Print a message prefixed with '===>' for visual distinction."""
    print(f'===> {phrase}')

def build_deck():
    """Build and return a full 52-card deck as a list of dicts"""
    deck = []
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    for suit in suits:
        for value in ranks:
            deck.append({'rank': value, 'suit': suit})
    return deck

def shuffle(deck):
    """Randomizes the order of the deck"""
    random.shuffle(deck)

def deal_card(deck, hand):
    """Removes card from deck, appends card to provided hand"""
    card = deck.pop()
    hand.append(card)

def calc_total(hand):
    """Calculates total of hand based on card value"""
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
    """Returns True if total is > TARGET_SCORE, False otherwise"""
    return total > TARGET_SCORE

def ace_value(score, hand):
    """Convert Aces from 11 to 1 as needed to bring score under 21, and return the new score"""
    aces = len([card['rank'] for card in hand if card['rank'] == 'Ace'])
    while score > TARGET_SCORE and aces >= 1:
        score -= 10
        aces -= 1
    return score

def player_hit():
    """Determines if player would like another card, if 'hit', returns True"""
    prompt('Would you like to hit or stay?')
    while True:
        response = input().strip().lower()
        if response in ['hit', 'stay']:
            return response == 'hit'
        prompt('That is not a valid input. Please choose hit or stay')

def score_comparison(player, dealer):
    """Compares player and dealer totals, returns message describing who won"""
    if player <= TARGET_SCORE and dealer <= TARGET_SCORE:
        if player == dealer:
            message = "The game ends in a tie."
            return message, 'tie'
        if player > dealer:
            winner = 'player'
            message = f'Player wins! Final score {player} - {dealer}'
            return message, winner
        message = f'Dealer wins! Final score {dealer} - {player}'
        winner = 'dealer'
        return message, winner
    if player > TARGET_SCORE:
        message = 'Player busted. Dealer wins.'
        winner = 'dealer'
        return message, winner
    message = 'Dealer busted. Player wins'
    winner = 'player'
    return message, winner

def display_hand(hand, hide_extra_cards=False):
    """Formats hand and determines if additional cards should be hidden, returns formatted string"""
    card_strings = []
    for card in hand:
        card_strings.append(f"{card['rank']} of {card['suit']}")
    if hide_extra_cards:
        display = [card_strings[0], 'Unknown']
        hand_string = ', '.join(display)
        return hand_string
    hand_string = ', '.join(card_strings)
    return hand_string

def game_loop():
    """Runs complete round of 21. Deals initial hands to player and dealer. 
    Runs player turn, then dealer if player didn't bust. Displays final result"""

    player_hand = []
    dealer_hand = []

    prompt(f'Welcome to {TARGET_SCORE}.')

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

    if player_score == TARGET_SCORE:
        message, result = score_comparison(player_score, dealer_score)
        print(message)
        return result

    while player_hit():
        deal_card(initial_deck, player_hand)
        print(f'You currently hold: {display_hand(player_hand)}')
        player_score = calc_total(player_hand)
        if is_busted(player_score):
            break
        print(f'Your current score is {player_score}')

    if is_busted(player_score):
        message, result = score_comparison(player_score, dealer_score)
        print(message)
        return result

    while dealer_score < CPU_HIT_LIMIT:
        deal_card(initial_deck, dealer_hand)
        dealer_score = calc_total(dealer_hand)

    print(f'''Final hands are Player: {display_hand(player_hand)}
            Dealer: {display_hand(dealer_hand)}''')
    message, result = score_comparison(player_score, dealer_score)
    print(message)
    return result

def play_again():
    """Prompts player for another round. Returns True if player responds 'yes'"""
    prompt('Would you like to play again?')
    while True:
        response = input().lower().strip()
        if response in ['yes', 'no']:
            return response == 'yes'
        prompt('That is not an accepted response. Please respond yes or no.')

def wins_comparison(pwins, dwins):
    """Compares player and dealer win totals. Prints an updated string"""
    if pwins > dwins:
        if pwins < WINS_NEEDED:
            prompt(f'Player leads {pwins} - {dwins}')
        else:
            prompt(f'Player wins best of 5. Final score: {pwins} - {dwins}')
    elif dwins > pwins:
        if dwins < WINS_NEEDED:
            prompt(f'Dealer leads {dwins} - {pwins}')
        else:
            prompt(f'Dealer wins best of 5. Final score: {dwins} - {pwins}')
    else:
        prompt(f'The score is tied: Player {pwins} - Dealer {dwins}')


player_wins = 0
dealer_wins = 0

while True:
    game_winner = game_loop()
    if game_winner == 'player':
        player_wins += 1
    elif game_winner == 'dealer':
        dealer_wins += 1

    wins_comparison(player_wins,dealer_wins)

    if WINS_NEEDED in (player_wins, dealer_wins):
        if play_again():
            player_wins = 0
            dealer_wins = 0
        else:
            break
