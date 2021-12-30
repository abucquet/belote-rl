# player class
# TODO be implemented

import numpy as np
import random
from typing import List, Tuple, Dict

from card_elements import Card, Deck

class BasePlayer:
	'''
	Class that defines actions for a player. By default, the player will play randomly.
	'''
    
    def __init__(self, lr: float = 0.1, gamma: float = 0.9):
        self.q_table = {}
        self.last_state = None
        self.last_action = None
        self.lr = lr
        self.gamma = gamma

    def choose_move(self, valid_moves: List[Card], current_state) -> Card:
    	'''
		By default, the BasePlayer chooses a random action
    	'''
    	self.last_state = current_state
    	self.last_action = valid_moves[0]
    	return valid_moves[0]

    def update_policy(points_gained: int, next_state) -> None:
    	'''
		At the end of each trick, the players will receive 
		the number of points they gained in that trick.
    	'''
    	self.q_table[self.last_state][self.last_action] = \
    		self.q_table[self.last_state][self.last_action] + \
    		self.lr * (
    			points_gained + self.gamma * np.max(q_table[next_state]) — q_table[stat][action]
    			)





