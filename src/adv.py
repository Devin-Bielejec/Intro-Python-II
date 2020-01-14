from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Fork", "It has unbelievable Power!")]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Spoon", "No other weapon like it!")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Knife", "KEKEKEKEKE NIFE")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Pot", "This pot can do all your cooking")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Button", "Better than buttons")]),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def startAdventure():
    end = False
    start = True
    while end == False:
        if start == True:
            newPlayer = Player(room["outside"])
            start = False
        print("\n")
        print(newPlayer.room.name)
        print(newPlayer.room.description)
        print("\n")
        if (len(newPlayer.room.items) == 0):
            print("There are no items in the room")
        else:
            print("The items in the room are: ")
            for itemInstance in newPlayer.room.items:
                print(f"  {itemInstance.name} ({itemInstance.description})\n")

        userInput = input(
            "Which way will you go? [n, s, e, w, or q to quit (or i for inventory)]:\n\n\n\n")

        try:
            if userInput == "n":
                newPlayer.room = newPlayer.room.n_to
            elif userInput == "s":
                newPlayer.room = newPlayer.room.s_to
            elif userInput == "e":
                newPlayer.room = newPlayer.room.e_to
            elif userInput == "w":
                newPlayer.room = newPlayer.room.w_to
            elif userInput == "i":
                print("Your inventory:\n")
                for invItem in newPlayer.inventory:
                    print(f"{invItem.name}\n")

                roomItemNames = [x.name for x in newPlayer.room.items]
                inventoryItemNames = [x.name for x in newPlayer.inventory]

                userInputItemAdd = input(
                    "Your options: 'Get <itemName>' \n 'Take <itemName> \n 'Drop <itemName> \n 'Remove <itemName>? \n")

                method = userInputItemAdd.split(" ")[0]
                itemToChange = userInputItemAdd.split(" ")[1]
                print(method, itemToChange, "awoeifjaoweijf", roomItemNames)
                if method == "get" or method == "take":
                    if itemToChange in roomItemNames:
                        print("here")
                        itemIndex = roomItemNames.index(itemToChange)
                        newPlayer.addItem(newPlayer.room.items[itemIndex])
                        newPlayer.room.removeItem(
                            newPlayer.room.items[itemIndex])
                    else:
                        print("That item is not in the room, so you cannot take it!")
                elif method == "drop" or method == "remove":
                    if itemToChange in inventoryItemNames:
                        itemIndex = inventoryItemNames.index(itemToChange)
                        current_room.addItem(newPlayer.inventory[itemIndex])
                        newPlayer.room.removeItem(
                            newPlayer.inventory[itemIndex])
                    else:
                        print(
                            "That item is not in your inventory, so you cannot drop it!")
            else:
                print("Incorrect command!\n\n")
        except:
            print("Incorrect command!\n\n")

        if userInput == "q":
            end = True


startAdventure()
