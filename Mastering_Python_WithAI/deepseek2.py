# 1️⃣Write code that asks the user for a fruit name.
# Print its price if it exists.
# Print "Fruit not found." if it does not.

fruit_prices = {
    "apple": 1.50,
    "banana": 0.80,
    "mango": 2.50,
    "orange": 1.25
}

x = input(f"Input a fruit name :")

for key , value in fruit_prices.items():
    if x in key :
        print(f"The price of {key} is {value}")
        break
else:
    print("Fruit not found")

x = input("Input a fruit name: ").lower()
if x in fruit_prices:
    print(f"The price of {x} is {fruit_prices[x]}")
else:
    print("Fruit not found")


# ___________________________________________________________________________________________________________________#

''''2️⃣
1. Print all inventory items in this format: `Item: x5` (e.g., `Arrow: x12`)
print("--- Your Inventory ---")
Your printing code here
2. Calculate the total number of all items you are carrying.
Your calculation code here
Print the total like this: "Total items: 39"'''

inventory = {
    "Gold Coin": 23,
    "Arrow": 12,
    "Healing Potion": 3,
    "Magic Sword": 1
}
print(f"All Stuff on inventory : ")
total = 0
for key , value in inventory.items():
    print(f"{key} : x{value}")
    total+=value
print(f"The total items on inventory : {total}")    


# ___________________________________________________________________________________________________________________#

''''3️⃣Write code to print the player's name and the first weapon in their weapons list.
Expected output: "Sirius wields a Greatsword.'''

player_data = {
    "name": "Sirius",
    "class": "Warrior",
    "level": 15,
    "equipment": {
        "weapons": ["Greatsword", "Dagger", "Crossbow"],
        "armor": "Plate Mail"
    }
}

# This one too complex no need 
# for key , value in player_data.items():
#     if isinstance (value, dict):
#         for inner_key,inner_value in value.items():
#           if inner_value == value['weapons']:
#             print(f"{player_data['name']} wields a {value['weapons'][0]}")

player_name = player_data['name']
first_weapon = player_data['equipment']['weapons'][0]
print(f"{player_name} wields a {first_weapon}.")