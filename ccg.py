class Card:
    def __init__(self, point_value, kind, card_desc):
        # point_value: how many points the card is worth
        self.point_value = point_value
        # kind: whether it's environmental or innovational
        self.kind = kind
        # card_desc: description of what the card does; if it's a draw card, discard, etc.
        self.card_desc = card_desc