class Card:
    def __init__(self, name, current_point_value, category, card_desc):
        self.name = name
        # current_point_value: how many points the card is worth
        self.current_point_value = current_point_value
        # what type of issue does it lead to?
        self.category = category
        # card_desc: description of what the card does; if it's a draw card, discard, etc.
        self.card_desc = card_desc

class Innovation_Card(Card):
    def __init__(self, name, current_point_value, card_desc):
        super().__init__(name, current_point_value, card_desc)

class Environmental_Card(Card):
    pass

class Cleanup_Card(Card):
    def __init__(self, name, current_point_value, card_desc, category, removal):
        super().__init__(name, current_point_value, card_desc, category)
        self.removal = removal
    pass