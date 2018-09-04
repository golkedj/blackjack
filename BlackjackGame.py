from random import randint
from Deck import *

class BlackjackGame():

    def __init__(self):
        card1 = randint(0, 12)
        card2 = randint(0, 12)
        self.deck = Deck()
        value1 = self.deck.get_card_value(card1)
        value2 = self.deck.get_card_value(card2)
        self.total = value1 + value2
        self.game_done = False
        self.busted = False
        self.has_ace = False

    def take_turn(self):
        bust_cards = 0
        for card in self.deck.cards:
            if card.get_value() + self.total > 21:
                bust_cards = bust_cards + 1

        bust_probability = bust_cards/13

        print("Dealer has " + str(self.total) + " and chance of busting is " + str(bust_probability))

        if not self.game_done:
            if self.total < 17:
                self.hit()

            if self.total > 16:
                print("Game is over")
                self.game_done = True
            if self.total > 21:
                print("Dealer busted!!")
                self.busted = True

    def hit(self):
        card = randint(0, 12)
        value = self.deck.get_card_value(card)
        if value == 1:
            temp_value = 11
            if ((self.total + temp_value) > 16) and ((self.total + value) < 22):
                value = temp_value
        self.total = self.total + value
        return self.total