from room import Room
from player import Player
from item import Item
# Declare all the rooms
room = {
    'Outside Cave Entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Fork", "It has unbelievable Power!")]),

    'Foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Spoon", "No other weapon like it!")]),

    'Grand Overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Knife", "KEKEKEKEKE NIFE")]),

    'Narrow Passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item("Pot", "This pot can do all your cooking")]),

    'Treasure Chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Button", "Better than buttons")]),
}


# Link rooms together

room['Outside Cave Entrance'].n_to = room['Foyer']
room['Foyer'].s_to = room['Outside Cave Entrance']
room['Foyer'].n_to = room['Grand Overlook']
room['Foyer'].e_to = room['Narrow Passage']
room['Grand Overlook'].s_to = room['Foyer']
room['Narrow Passage'].w_to = room['Foyer']
room['Narrow Passage'].n_to = room['Treasure Chamber']
room['Treasure Chamber'].s_to = room['Narrow Passage']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# [X] Prints the current room name
# [X] Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def startAdventure():

    end = False
    start = True
    while end == False:
        if start == True:
            newPlayer = Player("Outside Cave Entrance")
            current_room = room[newPlayer.current_room]
            start = False
        
        print(current_room.name)    
        print(current_room.description)

        print("The items in the room are: ")
        
        for item in current_room.items:
            print("{item} ({des})\n".format(item=item.name, des=item.description))

        userInput = input("Which way will you go? [n, s, e, w, or q to quit]:\n\n\n\n")
        
        commands = ["i","b"]

        #Navigation Start
        map = {
            "Outside Cave Entrance": ["n"],
            "Foyer": ["s","n","e"],
            "Grand Overlook": ["s"],
            "Narrow Passage":["w","n"],
            "Treasure Chamber": ["s"]
        }

        if userInput in map[current_room.name]:
            if userInput == "n":
                current_room = room[current_room.name].n_to
            elif userInput == "s":
                current_room = room[current_room.name].s_to
            elif userInput == "e":
                current_room = room[current_room.name].e_to
            elif userInput == "w":
                current_room = room[current_room.name].w_to
        elif userInput == "i":
            print("Your inventory:\n")
            for invItem in newPlayer.inventory:
                print(invItem.name)

            roomItemNames = [x.name for x in current_room.items]
            inventoryItemNames = [x.name for x in newPlayer.inventory]
            
            userInputItemAdd = input("Do you want to change your inventory? \n")
            method = userInputItemAdd.split(" ")[0]
            itemToChange = userInputItemAdd.split(" ")[1]

            if method == "get" or method == "take":
                if itemToChange in roomItemNames:
                    itemIndex = roomItemNames.index(itemToChange)
                    newPlayer.addItem(current_room.items[itemIndex])
                    current_room.removeItem(current_room.items[itemIndex])
                else:
                    print("That item is not in the room, so you cannot take it!")
            elif method == "drop" or method == "remove":
                if itemToChange in inventoryItemNames:
                    itemIndex = inventoryItemNames.index(itemToChange)
                    current_room.addItem(newPlayer.inventory[itemIndex])
                    newPlayer.removeItem(newPlayer.inventory[itemIndex])
                else:
                    print("That item is not in your inventory, so you cannot drop it!")
        else:
            print("Incorrect Command!")

        #Adding an item to the player inventory
        

        if userInput == "q":
            end = True

startAdventure()