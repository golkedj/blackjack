from Card import *

class Deck():
    def __init__(self):
        ace = Card(1, "ace")
        two = Card(2, "two")
        three = Card(3, "three")
        four = Card(4, "four")
        five = Card(5, "five")
        six = Card(6, "six")
        seven = Card(7, "seven")
        eight = Card(8, "eight")
        nine = Card(9, "nine")
        ten = Card(10, "ten")
        jack = Card(10, "jack")
        queen = Card(10, "queen")
        king = Card(10, "king")
        self.cards = [ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]

    def get_card_value(self, index):
        return self.cards[index].get_value()