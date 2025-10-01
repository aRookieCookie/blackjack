import random       #Imports random for shuffle


class Deck:                     #Creates the deck to draw cards from
    def __init__(self):         #When initialized
        self.suits = ['\u2665\uFE0F','\u2663\uFE0F','\u2660\uFE0F','\u2666\uFE0F']   #♥️♣️♠️♦️  #All Suits
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']           #All Ranks
        self.deck = []          #Creates a list to store all cards in

        for suit in self.suits:                     #For every suit
            for number in self.ranks:               #For every rank
                self.deck.append((suit + number))   #Create a card with the suit and number combined

    def shuffle(self):                  #Function for shuffling the deck
        random.shuffle(self.deck)       #Shuffles the deck

    def deal(self):                 #Deals a card into the hand
        return self.deck.pop()      #Removes the drawn card from the deck and returns for an append to hand


class Dealer:                           #Dealers Hand
    def __init__(self, deck):           #When initialized
        self.hand = []                  #Create a list for hand
        self.hand.append(deck.deal())   #Add starting card
        self.hand.append(deck.deal())   #Add starting card

    def show_hand(self):    #Function to return the hand of the dealer
        return self.hand    #Returns the dealers hand


class Player:                           #Players hand
    def __init__(self, deck):           #When initialized
        self.hand = []                  #it creates a list for hand
        self.hand.append(deck.deal())   #Add starting card
        self.hand.append(deck.deal())   #Add starting card

    def show_hand(self):    #Function to return the hand of the player
        return self.hand    #Return the players hand