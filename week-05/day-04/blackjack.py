# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
import random
secure_random = random.SystemRandom()

class Card:
    
    def __init__(self, color, value):
        self.color = color
        self.value = value

    
    def get_card_type(self):
        return "Card : " + self.color + " " + str(self.value)


class Deck:
    
    def __init__(self, number):
        self.number = number
        self.colors = ['Club', 'Diamonds', 'Hearts', 'Spades']
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.list_of_cards = []
        # for i in range(4):
        #     self.list_of_cards.append( Card(self.colors[i], secure_random.choice(self.values)))

        while (len(self.list_of_cards) <= number):
            new_card = self.create_random_card()
            if new_card not in self.list_of_cards:
                self.list_of_cards.append(new_card)


    def shuffle(self):
        secure_random.shuffle(self.list_of_cards)

    
    def draw(self):
        return  self.list_of_cards.pop()

    
    def create_random_card(self):
        card = Card(secure_random.choice(self.colors), secure_random.choice(self.values))
        return card


    


deck = Deck(20)
deck.shuffle()
print(deck)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
top_card = deck.draw()
# top_card.get_card_type()
print(type(top_card))
print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades

