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
                if length > 0:
                    i = random.randint(0,length-1)
                    global_Warming.pop(i).draw(player)
            elif category == 'Natural Resource Use':
                length = len(natural_Resource)
                if length > 0:
                    i = random.randint(0,length-1)
                    natural_Resource.pop(i).draw(player)
            elif category == 'Water Pollution':
                length = len(water_pollution)
                if length > 0:
                    i = random.randint(0,length-1)
                    water_pollution.pop(i).draw(player)
            elif category == 'Deforestation':
                length = len(deforestation)
                if length > 0:
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

# Innovation_Cards

space_Exploration = Innovation_Card("Space Exploration", 7, "Exploration", "More landmass means more space to do what we need to do, whether that's farming, research, or whatever, so we believe that finding a habitable planet elsehere in the universe could prove to be invaluable.", ["Natural Resource Use", "Global Warming"])
deep_Sea_Exploration = Innovation_Card("Deep Sea Exploration", 4, "Exploration", "We know almost as little about the seas that seperate us as we do about the space over our heads. If we can figure out a way to make use of what's below us, maybe intergalactic travel won't be as necessary as soon.", ["Natural Resource Use", "Global Warming"])

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
self_Driving_Cars = Innovation_Card("Self Driving Cars", 5, "Travel", "Beyond helping those with disabilities, self driving cars would help us be a little more efficient, in that we won't have to focus on driving and will therefore be able to focus on other tasks.", ["Natural Resource Use", "Global Warming"])
sustainable_Aviation = Innovation_Card("Sustainable Aviation", 9, "Travel", "if aviation were less expensive, travel across planet could be less expensive and we'd be able to collaborate with our peers in person more often, improving our efficiency, because as nice as the internet is, sometimes the lag hurts more than the communication helps.", ["Natural Resource Use", "Global Warming"])
accesible_Transportation = Innovation_Card("Accessible Public Transportation", 5, "Travel", "With access to more public transportation, people can save on gas and not have to spend as much in order to go places. This could ease up homelessness problems, open up job opportunities, and clear traffic up by a lot.", ["Natural Resource Use", "Global Warming"])
teleporation = Innovation_Card("Teleportation", 1, "Travel", "this one was mostly a joke. I mean, who doesn't want to be able to teleport places?", ["Natural Resource Use", "Globabl Warming"])

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
artifical_Intelligence = Innovation_Card("Artificial Intelligence", 8, "Computer Tech", "the smarter our computers get, the less we gotta do", ["Deforestation", "Water Pollution"])
cryptocurrency = Innovation_Card("Cryptocurrency", 3, "Computer Tech", "feel like i should not we're not techbros.", ["Deforestation", "Water Pollution"])
virtual_Reality = Innovation_Card("Virtual and Augmented Reality", 5, "Computer Tech", "there're a fair amount of tools that could help us in the long run with vr and ar, whether it comes to AR warning us of dangers in real time, or VR teaching us how to perform tasks without the stress of a live situation.", ["Deforestation", "Water Pollution"])
quantum_Computing = Innovation_Card("Quantum Computing", 7, "Computer Tech", "who doesn't want more powerful computing?", ["Deforestation", "Water Pollution"])

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
panacea = Innovation_Card("Cure for All Diseases", 10, "Medical", "Although we have many cures for a few different disease, it is highly unrealistic for us to assume that a true panacea will ever be made. Just as humans keep evolving, so too do diseases, so in this infinite arms race there will be no true winners.", ["Water Pollution", "Deforestation"])
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

# Radical Innovation Cards

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

'''one = []
two = []
counter = [0]

if len(counter) % 2 == 0:
    space_Exploration.draw(one)
else:
    space_Exploration.draw(two)
counter.append(0)

if len(counter) % 2 == 0:
    deep_Sea_Exploration.draw(one)
else:
    deep_Sea_Exploration.draw(two)
counter.append(0)

if len(counter) % 2 == 0:
    self_Driving_Cars.draw(one)
else:
    self_Driving_Cars.draw(two)
counter.append(0)

if len(counter) % 2 == 0:
    sustainable_Aviation.draw(one)
else:
    sustainable_Aviation.draw(two)

if len(counter) % 2 == 0:
    accesible_Transportation.draw(one)
else:
    accesible_Transportation.draw(two)

if len(counter) % 2 == 0:
    teleporation.draw(one)
else:
    teleporation.draw(two)
counter.append(0)
counter.append(0)
counter.append(0)
hand1 = []
hand2 = []
for i in one:
    hand1.append(i.name)
for j in two:
    hand2.append(j.name)
print(hand1)
print(hand2)'''
'''
deep_Sea_Exploration.draw(player)
for thing in player:
    print(thing.name)
print()

harmful_Gas_Filtering.draw(player)
for thing in player:
    print(thing.name)
print()

for thing in one:
    print(thing.name)
print()

for thing in two:
    print(thing.name)
print()
player = one

self_Driving_Cars.draw(player)
for thing in player:
    print(thing.name)'''
