# TODO: add comments

import random

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):        
        return "{0} {1}".format(self.value,self.suit)
    

class Deck: 
    '''
    TODO: implement two new functions
        self.deal: deals the cards in the deck to four players
            return a list of hands (lists of cards)
        self.toArray: create an np.array with features that will be used in the model
    '''


    def __init__(self, values, suits):
        self.cards = []
        self.populate(values,suits)
        self.shuffle()
        
    def __str__(self):
        deck = ", ".join([str(card) for card in self.cards])
        side = ", ".join([str(card) for card in self.side_pile])
        return deck + "/" + side

    def populate(self, values, suits):
        for suit in suits:
            for value in values:
                thisCard = Card(suit,value)
                self.cards.append(thisCard)  
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n_hands):
        hand_size = len(self.cards)//n_hands

        return [
            self.cards[i*hand_size:(i+1)*hand_size] for i in range(n_hands)
        ]

    def print_all(self):  
        print("Deck:", end=" ")
        for card in self.cards:
            print(card, end=" ")
        print("")

    def copy(self, deep=True):
        new_deck = Deck([1], ["A"])
        new_deck.cards = self.cards[:]
        return new_deck