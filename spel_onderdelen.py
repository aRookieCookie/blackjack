import random


class Deck:
    def __init__(self):
        self.suits = ['\u2665\uFE0F','\u2663\uFE0F','\u2660\uFE0F','\u2666\uFE0F']   #♥️♣️♠️♦️
        # self.ranks = ['A', '2']
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []

        for suit in self.suits:
            for number in self.ranks:
                self.deck.append((suit + number))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Dealer:
    def __init__(self, deck):
        self.hand = []
        self.hand.append(deck.deal())
        self.hand.append(deck.deal())

    def show_hand(self):
        return self.hand


class Player:
    def __init__(self, deck):
        self.hand = []
        self.hand.append(deck.deal())
        self.hand.append(deck.deal())

    def show_hand(self):
        return self.hand