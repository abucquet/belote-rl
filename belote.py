
# Mechanics of the game of belote
import random
from typing import List, Tuple, Dict

from card_elements import Card, Deck

# constants
VALUES = ["A", "K", "Q", "J", "10", "9", "8", "7"]
SUITS = { #keys are unicode symbols for suits
    u'\u2660': "black",
    u'\u2665': "red",
    u'\u2663': "black",
    u'\u2666': "red",
}
DECK = Deck(VALUES, SUITS)
PLAYERS = ["North", "East", "South", "West"] 
TEAMS = {
	"North": 0, 
	"East": 1,
	"South": 0,
	"West": 1
	} #teams: N-S and E-W

def play_trick(player_starting: int, hands: List[List[Card]]) -> Tuple[int]:
	'''
	Plays one trick, with |player_starting| playing a card first.

	Returns a tuple containing:
		the new player starting
		the number of points in the trick
	Edits the |hands| list to reflect the cards that have been played.
	'''
	# TODO: implement
	pass


def play_hand(current_scores : List[int], current_round: int):
	'''
	Plays one hand (8 tricks). |current_round| is used to know who starts.

	Updates |current scores| once the hand is done.
	'''
	hand_scores = [0, 0]

	DECK.shuffle()
	hands = DECK.deal()
	player_starting = current % len(PLAYERS)
	
	for i in range(len(VALUES)):
		player_starting, hand_points = play_trick(player_starting, hands)
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
		play_hand(scores)
		rounds_played += 1