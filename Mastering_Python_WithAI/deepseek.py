# This is our complex, nested dictionary. It's our "monster" to explore.
game_data = {
    "player": {
        "name": "Anna",
        "level": 5,
        "inventory": {
            "gold": 250,
            "weapons": ["Sword", "Dagger"],
            "potions": {
                "health": 3,
                "mana": 1
            }
        }
    },
    "locations": [
        {
            "name": "Forest",
            "enemies": ["Goblin", "Wolf"]
        },
        {
            "name": "Cave",
            "enemies": ["Dragon", "Bat"],
            "quest_available": True
        }
    ]
}

print("Game Data Monster created! Let's explore it.")

def get_player_name(data):
    """Accesses the nested player's name"""
    # data['player'] gets us the inner dictionary
    # Then we get the 'name' key from THAT dictionary
    player_name = data['player']['name']
    print(f"The player's name is: {player_name}")

# Call the function
get_player_name(game_data)

def list_player_weapons(data):
    """Lists all the weapons in the player's inventory"""
    # Get the list of weapons
    weapons_list = data['player']['inventory']['weapons']
    print("Player's Weapons:")
    # Now we loop through the list!
    for weapon in weapons_list:
        print(f" - {weapon}")

list_player_weapons(game_data)

def count_health_potions(data):
    """sum of health potions"""
    health_potion_count = data['player']['inventory']['potions']['health']
    print(f"The amount of healt potions player have is {health_potion_count}")
count_health_potions(game_data)

def explore_dict(data, indent=0):
    """Recursively explores and prints a nested dictionary structure."""
    # Create an indent string to show depth (2 spaces per level)
    indent_str = "  " * indent

    # Check if the thing we're exploring is a dictionary
    if isinstance(data, dict):
        for key, value in data.items(): # .items() gives us (key, value) pairs
            print(f"{indent_str}{key}: ")
            # Now, explore the VALUE recursively! It might be another dict, a list, or something else.
            explore_dict(value, indent + 1) # <-- The magic is here. We call ourselves!
    # Check if it's a list
    elif isinstance(data, list):
        for item in data:
            explore_dict(item, indent + 1) # Explore each item in the list
    else:
        # If it's not a dict or list, it's a basic value (string, number, boolean)
        print(f"{indent_str}{data}")

# Let's run our explorer on the monster!
print("\n=== EXPLORING THE GAME DATA MONSTER ===")
explore_dict(game_data)