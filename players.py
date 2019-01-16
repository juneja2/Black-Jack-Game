
from card import Card
import shapes

class Player():
    
    def __init__(self, money=100):
        self.cards = []
        self.sum = 0
        self.aces = 0
        self.money = money

    def append(self):
        card, suite = Card.get_random_card()
        value = 0
        if card == "A":
            if self.aces == 1:
                self.aces = 0
                value = 1
            else:
                self.aces = 1
                value = 11
            
        elif card in "KQJ" :
            value = 10

        elif 1 <= int(card) <= 10:
            value = int(card)

        self.sum += value
        self.cards.append(Card(card, value, suite))
        Card.change_deck(card, suite)

    def print_player_cards(self, player_turn = True):

        
        # 11 is the number of strings required to print a card
            for i in range(11):
                card_row = ""
                if player_turn:
                    for card in self.cards:
                        card_row += card.card_str_array()[i] + " "
                    print(card_row)
                else:
                    card_row = shapes.empty()[i]
                    print(self.cards[0].card_str_array()[i] + " " + card_row)



if __name__ == "__main__":
    p = Player()
    p.append()
    p.append()
    p.append()
    p.append()
    p.print_player_cards(False)
    p.print_player_cards()


        

            
        
        




    