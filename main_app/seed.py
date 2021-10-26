from .models import Ingredient


Vegetables = [
   'Artichoke', 'Arugula' , 'Asparagus', 'Beet'
, 'Broccoli', 'Brussels Sprout', 'Cabbage', 'Cauliflower'
, 'Carrot','Celery','Chard', 'Chili Pepper'
, 'Collards', 'Cucumber','Eggplant', 'Endive'
, 'Fennel','Garlic','Green Bean', 'Iceberg_Lettuce'
, 'Kale','Leek', 'Mushroom','Nettle'
, 'Okra', 'Onion', 'Parsnip', 'Peas'
, 'Potato', 'Radish', 'Soybean', 'Spinach'
, 'Sunchoke', 'Sweet_Potato', 'Tomato', 'Turnip'
, 'Yams', 'Zucchini', 'Butternut Squash', 'Squash'
, 'Habanero Pepper', 'Horseradish', 'Bell Peppers', 'Peppers'
, 'Jalapeno Pepper', 'Lettuce', 'Serrano Pepper', 'Poblano Pepper'
, 'Romaine Lettuce', 'Escarole Lettuce', 'Bibb Lettuce', 'Radicchio'
, 'Acorn Squash', 'Ramps', 'Broccolini', 'Chickpea'
, 'Shallot', 'Scallion', 'Seaweed', 'Celery Root'
, 'Bok Choy', 'Fiddlehead Fern', 'Hearts of Palm', 'Jicama'
, 'Lemongrass', 'Pumpkin', 'Rhubarb', 'Tomatillo', 'Capers'
, 'Black Eyed Peas', 'Lima Beans', 'Water Chestnuts', 'Aloe Vera'
, 'BroccoLeaf'
]

for veg in Vegetables:
    ingred = {
            'type': 'Vegetable',
            'category': 'vegan',
        }
    ingred.__setitem__("name", veg)
    new_ingred = Ingredient.objects.create(type=ingred.get("type"), catergory=ingred.get("category"), name=ingred.get("name"))
    new_ingred.save()
    # print('list of veggies',ingred)
all_ingreds = Ingredient.objects.all()
print(list(all_ingreds))

Fruits = [
   " Apples", 
   "Apricot", 
   "Avocado",
    "Banana", 
    "Blackberry", 
    "Blueberry", 
    "Boysenberry",
    "Cherry", 
    "Cranberry", 
    "Date", 
    "Fig",
    "Grapefruit", 
    "Grape",
    "Guava",
    "Honeydew",
    "Kiwi",
    "Kumquat",
    "Lemon", 
    "Mango",
    "Nectarine",
    "Olives", 
    "Orange",
    "Papaya",
    "Peach",
    "Pear", 
    "Pineapple", 
    "Plum",
    "Prune", 
    "Pomegranate", 
    "Quince", 
    "Raspberry",
    "Strawberry", 
    "Watermelon", 
    "Jackfruit", 
    "Starfruit",
    "Huckleberry", 
    "Asian_Pear", 
    "Gooseberry", 
    "Jujube",
    "Lychee", 
    "Blood_Orange", 
    "Persimmon", 
    "Ugli_Fruit",
    "Yuzu", 
    "Tamarind", 
    "Goji_Berry", 
    "Lingonberry", 
    "Cherimoya",
    "Lime", 
    "Mandarin", 
    "Cantaloupe"
]
for fruit in Fruits:
    ingred = {
            'type': 'Fruits',
            'category': 'vegan',
        }
    ingred.__setitem__("name", fruit)
    # print('list of fruits',ingred)

Grains = [
    "Amaranth", 
    "Barley", 
    "Buckwheat", 
    "Bulgur", 
    "Corn", 
    "Oats", 
    "Quinoa", 
    "Rye",
    "Wheat", 
    "Rice", 
   "Couscous"
]
for grain in Grains:
    ingred = {
            'type': 'Grains',
            'category': 'carbohydrate',
        }
    ingred.__setitem__("name", grain)
    # print('list of grain',ingred)
Herbs = [
    "Basil", 
    "Bay_leaf", 
    "Dill", 
    "Lavender",
    "Lemonbalm",
    "Mint",
    "Oregano",
    "Parsley",
    "Rosemary",
    "Sage",
    "Tarragon",
    "Thyme",
    "Wheatgrass",
    "Cilantro",
    "Chives",
    "Shiso",
    "Savory",
    "Chamomile",
    "Dandelion_Root",
    "Hibiscus"
]
for herb in Herbs:
    ingred = {
            'type': 'Herbs',
            'category': 'vegan',
        }
    ingred.__setitem__("name", herb)

    # print('list of herbs',ingred)
Nuts = [
    "Almond", 
    "Cashew", 
    "Chestnut", 
    "Coconut",
    "Macadamia", 
    "Peanuts", 
    "Pecans", 
    "Pine_Nuts",
    "Pistachio", 
    "Walnut", 
    "Brazil_Nuts", 
    "Kola_Nuts",
]
for nut in Nuts:
    ingred = {
            'type': 'Nuts',
            'category': 'vegetarian',
        }
    ingred.__setitem__("name", nut)
    # print('list of nuts',ingred)

Seeds = [
    "Chia", 
    "Flax_seed", 
    "Sesame", 
    "Poppy_Seeds",
    "Mustard_Seed", 
    "Caraway_Seeds", 
    "Celery_Seed", 
    "Wild_Rice",
    "Coffee_Bean",
    "Cocoa_Bean",

]
for seed in Seeds:
    ingred = {
            'type': 'Seeds',
            'category': 'vegan',
        }
    ingred.__setitem__("name", seed)
    # print('list of herbs',ingred)

Spices = [
    "Cardamom", 
    "Cayenne", 
    "Cinnamon", 
    "Clove",
    "Coriander", 
    "Ginger", 
    "Juniper", 
    "Vanilla",
    "Turmeric", 
    "Anise", 
    "Peppercorn", 
    "Fenugreek",
    "Cumin", 
    "Mace", 
    "Salt", 
    "Allspice",
    "Saffron", 
    "Licorice",
]
for spice in Spices:
    ingred = {
            'type': 'Spices',
            'category': 'vegan',
        }
    ingred.__setitem__("name", spice)
    # print('list of herbs',ingred)

Meats = []