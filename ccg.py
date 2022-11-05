class Card:
    def __init__(self, name, current_point_value, category, card_desc):
        self.name = name
        # current_point_value: how many points the card is worth
        self.current_point_value = current_point_value
        # what type of issue does it lead to?
        self.category = category
        # card_desc: description of what the card does; if it's a draw card, discard, etc.
        self.card_desc = card_desc

#positive point values, varying.
class Innovation_Card(Card):
    def __init__(self, name, current_point_value, category, card_desc, cost):
        super().__init__(name, current_point_value, category, card_desc)
        #cost: list of categories that will be pulled when this innovation card is drawn.
        self.cost = cost

#negatice point values, the same.
class Environmental_Card(Card):
    pass

#0 point values
class Cleanup_Card(Card):
    def __init__(self, name, current_point_value, card_desc, category, removal):
        super().__init__(name, current_point_value, card_desc, category)
        #removal: Specific Category of cards that this card can remove from a player's hand.
        self.removal = removal
    pass
