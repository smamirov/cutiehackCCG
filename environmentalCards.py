from ccg import Card, Environmental_Card

# Global Warming Cards
generatingPower = Environmental_Card("Generating Power", -5, "Global Warming", "Description")
manufacturingGoods = Environmental_Card("Manufacturing Goods", -1, "Global Warming", "Description")
usingTransportation = Environmental_Card("Using Transportation", -4, "Global Warming", "Description")
foodProduction = Environmental_Card("Food Production", -4, "Global Warming", "Description")

# Natural Resource Use Cards
water = Environmental_Card("Water", -5, "Natural Resource Use", "Description")
oil = Environmental_Card("Oil", -2, "Natural Resource Use", "Description")
naturalGas = Environmental_Card("Natural Gas", -2, "Natural Resource Use", "Description")
plantsAndAnimals = Environmental_Card("Plants and Animals", -3, "Natural Resource Use", "Description")

# Water Pollution Cards
industrialWaste = Environmental_Card("Industrial Waste", -5, "Water Pollution", "Description")
marineDumping = Environmental_Card("Marine Dumping", -4, "Water Pollution", "Description")
sewageAndWastewater = Environmental_Card("Sewage and Wastewater", -3, "Water Pollution", "Description")
oilLeaks = Environmental_Card("Oil Leaks and Spills", -4, "Water Pollution", "Description")

# Deforestation Cards
timberLogging = Environmental_Card("Timber Logging", -5, "Deforestation", "Description")
mining = Environmental_Card("Mining", -5, "Deforestation", "Description")
expansion = Environmental_Card("Expansion and Infrastructure", -5, "Deforestation", "Description")
climateChange = Environmental_Card("Climate Change", -5, "Deforestation", "Description")

# Test
print(generatingPower.name, generatingPower.category, generatingPower.current_point_value, generatingPower.card_desc)

