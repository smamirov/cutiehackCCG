from ccg import Innovation_Card
space_Exploration = Innovation_Card("Space Exploration", 7, "Exploration", "insert string here", ["NaturalResourceUse", "Global Warming"])
Deep_Sea_Exploration = Innovation_Card("Deep Sea Exploration", 4, "Exploration", "insert string here", ["NaturalResourceUse", "Global Warming"])

exploration = [space_Exploration,Deep_Sea_Exploration]
for thing in exploration:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()

self_Driving_Cars = Innovation_Card("Self Driving Cars", 5, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
sustainable_Aviation = Innovation_Card("Sustainable Aviation", 9, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
accesible_Transportation = Innovation_Card("Accessible Public Transportation", 5, "Travel", "insert string here", ["NaturalResourceUse", "Global Warming"])
teleporation = Innovation_Card("Teleportation", 1, "Travel", "insert string here", ["NaturalResourceUse", "Globabl Warming"])

travel = [self_Driving_Cars, sustainable_Aviation, accesible_Transportation, teleporation]
for thing in travel:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()

artifical_Intelligence = Innovation_Card("Artificial Intelligence", 8, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
cryptocurrency = Innovation_Card("Cryptocurrency", 3, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
virtual_Reality = Innovation_Card("Virtual and Augmented Reality", 5, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])
quantum_Computing = Innovation_Card("Quantum Computing", 7, "Computer Tech", "insert string here", ["Deforestation", "Water Pollution"])

computer_Tech = [artifical_Intelligence, cryptocurrency, virtual_Reality, quantum_Computing]
for thing in computer_Tech:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()

panacea = Innovation_Card("Cure for All Diseases", 10, "Medical", "insert string here", ["Water Pollution", "Deforestation"])
food = Innovation_Card("Printable Food", 10, "Medical", "insert string here", ["Water Pollution", "Deforestation"])

medical = [panacea, food]
for thing in medical:
    print(thing.name)
    print(thing.current_point_value)
    print(thing.category)
    print(thing.card_desc)
    print(thing.cost)
    print()