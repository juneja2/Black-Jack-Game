import shapes
from random import randint

def deck_of_cards():
    deck = {}
    deck["10"] = {"Diamond": 1, "Heart":1, "Spade":1, "Club":1}
    for face in "A23456789KQJ":
        deck[face] = {"Diamond":1, "Heart":1, "Spade":1, "Club":1}

    return deck

class Card():
    deck_left = deck_of_cards()

    def __init__(self, face, val, suite):
        self.face = face
        self.val = val
        self.suite = suite

    @classmethod
    def change_deck(cls, card, suite):
        cls.deck_left[card][suite] = 0

    @classmethod
    def card_in_deck(cls, c, s):
        return cls.deck_left[c][s] == 1

    @staticmethod
    def random_face():
        card = randint(1, 13)
        if card == 1:
            return "A"
        elif card <= 10:
            return str(card)
        elif card == 11:
            return "J"
        elif card == 12:
            return "Q"
        else:
            return "K"

    @staticmethod
    def random_suite():
        suite = randint(1, 4)
        if suite == 1:
            return "Diamond"
        elif suite == 2:
            return "Heart"
        elif suite == 3:
            return "Spade"
        else:
            return "Club"
    @staticmethod
    def get_random_card():
        while True:
            c = Card.random_face()
            s = Card.random_suite()
            if Card.card_in_deck(c, s):
                return c, s

    def card_str_array(self):
        if self.suite == "Diamond":
            return shapes.diamond(self.face)
        elif self.suite == "Heart":
            return shapes.heart(self.face)
        elif self.suite == "Spade":
            return shapes.spade(self.face)
        elif self.suite == "Club":
            return shapes.club(self.face)    

    def __str__(self):
        
        card_blue_print = self.card_str_array()
        
        card_blue_print_array = ""

        for strings in card_blue_print:
            card_blue_print_array += strings + "\n"

        return card_blue_print_array


if __name__ == "__main__":
    A = Card("10", 10,  "Club" )
    print(A)
    

