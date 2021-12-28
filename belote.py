
# Mechanics of the game of belote
import random
from typing import List, Tuple, Dict

from card_elements import Card, Deck

# constants
VALUES = ["7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = { #keys are unicode symbols for suits
    u'\u2660': "black",
    u'\u2665': "red",
    u'\u2663': "black",
    u'\u2666': "red",
}
NON_TRUMP_ORDER = ["7", "8", "9", "J", "Q", "K", "10", "A"]
TRUMP_ORDER = ["7", "8", "Q", "K", "10", "A", "9", "J"]
NON_TRUMP_POINTS = {
	"7": 0, "8": 0, "9": 0, "J": 2, "Q" : 3, "K": 4, "10": 10, "A": 11
	}
TRUMP_POINTS = {
	"7": 0, "8": 0, "Q": 3, "K": 4, "10": 10, "A": 11, "9": 14, "J": 20
	}

DECK = Deck(VALUES, SUITS)
PLAYERS = ["North", "East", "South", "West"]
TEAMS = {
	"North": 0, 
	"East": 1,
	"South": 0,
	"West": 1
	} #teams: N-S and E-W

def find_valid_moves(hand: List[Card], played_in_trick: List[Card], trump_suit) -> List[Card]:
	'''
	Finds the cards from |hand| that are valid plays for the given trick, taking into
	account the cards that have already been played (|played_in_trick|).
	'''
	if len(played_in_trick) == 0:
		# a player starting a trick can play whatever they want
		return hand

	suit_asked = played_in_trick[0].suit

	allowable_cards = []
	for card in hand:
		if card.suit == suit_asked:
			allowable_cards.append(card)

	if len(allowable_cards) != 0: 
		# if you have the suit that was asked, you have to play that suit
		return allowable_cards

	# otherwise, you have to trump
	for card in hand:
		if card.suit == trump_suit:
			allowable_cards.append(card)

	# unless your partner is winning already
	if len(played_in_trick) - find_winning_card(hand, trump_suit) == 2:
		return hand

	# or you don't have trump cards
	if len(allowable_cards) == 0:
		return hand

	return allowable_cards

def is_beaten_by(card1: Card, card2: Card, trump_suit) -> bool:
	'''
	Compares two cards. Returns true if card2 beats card1
	'''
	if card2.suit == trump_suit:
		if card1.suit != trump_suit:
			# trump beats non-trump, or high value wins
			return True

		return TRUMP_ORDER.index(card1.value) < TRUMP_ORDER.index(card2.value)

	if card2.suit == card1.suit:
		# if non-trump, must be same suit and higher value
		return NON_TRUMP_ORDER.index(card1.value) < NON_TRUMP_ORDER.index(card2.value)

	return False

def find_winning_card(cards: List[Card], trump_suit) -> int:
	'''
	Returns the index of the card that wins the hand
	'''
	best_i = 0
	best_card = cards[0]

	for cur_i in range(1, len(cards)):
		cur_card = cards[cur_i]
		if is_beaten_by(best_card, cur_card, trump_suit):
			best_i = cur_i
			best_card = cur_card

	return best_i

def play_trick(player_starting: int, hands: List[List[Card]], trump_suit) -> Tuple[int]:
	'''
	Plays one trick, with |player_starting| playing a card first.

	Returns a tuple containing:
		the new player starting
		the number of points in the trick
	Edits the |hands| list to reflect the cards that have been played.
	'''
	next_up = player_starting
	cards_played = []

	for _ in range(len(PLAYERS)):
		valid_moves = find_valid_moves(hands[next_up], cards_played, trump_suit)
		card_played = hands[next_up][0]
		cards_played.append(card_played)
		hands[next_up].remove(card_played)
		next_up = (next_up + 1) % len(PLAYERS)

	winner = find_winning_card(cards_played, trump_suit)

	points_scored = sum(
		[NON_TRUMP_POINTS[card.value] \
			if card.suit != trump_suit \
			else TRUMP_POINTS[card.value]\
			for card in cards_played]
		)
	if len(hands[0]) == 0:
		points_scored += 10 # las trick is worth 10 extra points

	return winner, points_scored


def play_hand(current_scores : List[int], current_round: int):
	'''
	Plays one hand (8 tricks). |current_round| is used to know who starts.

	Updates |current scores| once the hand is done.
	'''
	hand_scores = [0, 0]

	DECK.shuffle()
	hands = DECK.deal(4)
	trump_suit = random.choice(list(SUITS.keys()))
	player_starting = current_round % len(PLAYERS)
	
	for i in range(len(VALUES)):
		player_starting, hand_points = play_trick(player_starting, hands, trump_suit)
		hand_scores[TEAMS[PLAYERS[player_starting]]] += hand_points

	# TODO: assess whether the contract was completed
	current_scores[0] += hand_scores[0]
	current_scores[1] += hand_scores[1]

def play_game(score_target: int):
	'''
	Plays a game to |score_target| points
	'''

	scores = [0, 0] # N-S and E-W
	rounds_played = 0

	while scores[0] < score_target and scores[1] < score_target:
		play_hand(scores, rounds_played)
		rounds_played += 1
		print(rounds_played, scores)

if __name__ == "__main__":
	play_game(500)






