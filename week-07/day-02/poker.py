import random
secure_random = random.SystemRandom()

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return self.color + self.value


class Deck:
    def __init__(self):
        self.colors = ['C', 'D', 'H', 'S']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.list_of_cards = []
        for color in self.colors:
            for value in self.values:
                self.list_of_cards.append(Card(color,value))


    def get_random_card(self):
        secure_random.shuffle(self.list_of_cards)
        return self.list_of_cards.pop()


class Hand:
    def __init__(self):
        self.hands_cards_list = []

    def fill_up_hands(self, card):
        self.hands_cards_list.append(card)

    def __repr__(self):
        hand_card = ""
        for card in self.hands_cards_list:
            hand_card += card.__repr__() +"\n" 
        return hand_card

deck = Deck()
hand01 = Hand()
hand02 = Hand()
print(hand01.fill_up_hands(deck.get_random_card()))




    
    

