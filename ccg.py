import random

class Card:
    def __init__(self, name, current_point_value, category, card_desc):
        self.name = name
        # current_point_value: how many points the card is worth
        self.current_point_value = current_point_value
        # what type of issue does it lead to?
        self.category = category
        # card_desc: description of what the card does; if it's a draw card, discard, etc.
        self.card_desc = card_desc

    #draw: a specific card is drawn. This function adds this card to the player's list of cards.
    def draw(self, player):
        player.append(self)
        return

#positive point values, varying.
class Innovation_Card(Card):
    def __init__(self, name, current_point_value, category, card_desc, cost):
        super().__init__(name, current_point_value, category, card_desc)
        #cost: list of categories that will be pulled when this innovation card is drawn.
        self.cost = cost

    def draw(self, player):
        super().draw(player)
        for category in self.cost:
            if category == 'Global Warming':
                length = len(global_Warming)
                i = random.randint(0,length-1)
                global_Warming.pop(i).draw(player)
            elif category == 'Natural Resource Use':
                length = len(natural_Resource)
                i = random.randint(0,length-1)
                natural_Resource.pop(i).draw(player)
            elif category == 'Water Pollution':
                length = len(water_pollution)
                i = random.randint(0,length-1)
                water_pollution.pop(i).draw(player)
            elif category == 'Deforestation':
                length = len(deforestation)
                i = random.randint(0,length-1)
                deforestation.pop(i).draw(player)
            else:
                print("something messed up")
                return -1
        return

#negatice point values, the same.
class Environmental_Card(Card):
    pass

#0 point values
class Cleanup_Card(Card):
    def __init__(self, name, current_point_value, card_desc, category, removal):
        super().__init__(name, current_point_value, card_desc, category)
        #removal: Specific Category of cards that this card can remove from a player's hand.
        self.removal = removal
    
    def draw(self, player):
        super().draw(player)
        for card in player:
            if card.category == self.removal:
                player.pop(player.index(card))
                return
        print('no matching cards found!')
        return
    pass

##########################################
#               CARDS BELOW              #
# Testing below that. please don't look. #
##########################################


# Global Warming Cards
generatingPower = Environmental_Card("Generating Power", -5, "Global Warming", "Description")
manufacturingGoods = Environmental_Card("Manufacturing Goods", -1, "Global Warming", "Description")
usingTransportation = Environmental_Card("Using Transportation", -4, "Global Warming", "Description")
foodProduction = Environmental_Card("Food Production", -4, "Global Warming", "Description")
global_Warming = [generatingPower, manufacturingGoods, usingTransportation, foodProduction]

# Natural Resource Use Cards
water = Environmental_Card("Water", -5, "Natural Resource Use", "Description")
oil = Environmental_Card("Oil", -2, "Natural Resource Use", "Description")
naturalGas = Environmental_Card("Natural Gas", -2, "Natural Resource Use", "Description")
plantsAndAnimals = Environmental_Card("Plants and Animals", -3, "Natural Resource Use", "Description")
natural_Resource = [water, oil, naturalGas, plantsAndAnimals]

# Water Pollution Cards
industrialWaste = Environmental_Card("Industrial Waste", -5, "Water Pollution", "Description")
marineDumping = Environmental_Card("Marine Dumping", -4, "Water Pollution", "Description")
sewageAndWastewater = Environmental_Card("Sewage and Wastewater", -3, "Water Pollution", "Description")
oilLeaks = Environmental_Card("Oil Leaks and Spills", -4, "Water Pollution", "Description")
water_pollution = [industrialWaste,marineDumping,sewageAndWastewater, oilLeaks]

# Deforestation Cards
timberLogging = Environmental_Card("Timber Logging", -5, "Deforestation", "Description")
mining = Environmental_Card("Mining", -5, "Deforestation", "Description")
expansion = Environmental_Card("Expansion and Infrastructure", -5, "Deforestation", "Description")
climateChange = Environmental_Card("Climate Change", -5, "Deforestation", "Description")
deforestation = [timberLogging, mining, expansion, climateChange]

space_Exploration = Innovation_Card("Space Exploration", 7, "Exploration", "insert string here", ["Natural Resource Use", "Global Warming"])
deep_Sea_Exploration = Innovation_Card("Deep Sea Exploration", 4, "Exploration", "insert string here", ["Natural Resource Use", "Global Warming"])

exploration = [space_Exploration, deep_Sea_Exploration]
'''
for thing in exploration:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()
'''
self_Driving_Cars = Innovation_Card("Self Driving Cars", 5, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
sustainable_Aviation = Innovation_Card("Sustainable Aviation", 9, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
accesible_Transportation = Innovation_Card("Accessible Public Transportation", 5, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
teleporation = Innovation_Card("Teleportation", 1, "Travel", "insert string here", ["NaturalResourceUse", "Globabl Warming"])

travel = [self_Driving_Cars, sustainable_Aviation, accesible_Transportation, teleporation]
'''
for thing in travel:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()
'''
artifical_Intelligence = Innovation_Card("Artificial Intelligence", 8, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
cryptocurrency = Innovation_Card("Cryptocurrency", 3, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
virtual_Reality = Innovation_Card("Virtual and Augmented Reality", 5, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
quantum_Computing = Innovation_Card("Quantum Computing", 7, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])

computer_Tech = [artifical_Intelligence, cryptocurrency, virtual_Reality, quantum_Computing]
'''
for thing in computer_Tech:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()
'''
panacea = Innovation_Card("Cure for All Diseases", 10, "Medical", "insert string here", ["Water Pollution", "Deforestation"])
food = Innovation_Card("Printable Food", 10, "Medical", "insert string here", ["Water Pollution", "Deforestation"])

medical = [panacea, food]
'''
for thing in medical:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()
'''
harmful_Gas_Filtering = Cleanup_Card("Harmful Gas Filtering", 0, "Radical Innovations", "desc", "Global Warming")
nuclear_Energy = Cleanup_Card("Nuclear Energy", 0,"Radical Innovations", "desc", "Natural Resource Use")
reforestation = Cleanup_Card("Reforestation",0,"Radical Innovations", "desc", "Deforestation")
absorb_Oil = Cleanup_Card("Absorb All Oil Wastes", 0, "Radical Innovation", "desc", "Water Pollution")

cleanup_cards = [harmful_Gas_Filtering,nuclear_Energy,reforestation, absorb_Oil]
'''
for thing in cleanup_cards:
    print(thing.name)
    print(thing.removal)
    print()
'''

### TESTING ###
player = []
deep_Sea_Exploration.draw(player)
for thing in player:
    print(thing.name)
print()
harmful_Gas_Filtering.draw(player)
for thing in player:
    print(thing.name)
