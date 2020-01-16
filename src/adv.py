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
    start = True
    newPlayer = Player(room["outside"])
    while start == True:
        #Description
        print(newPlayer.currentRoom)
        #Items in the room
        print(newPlayer.currentRoom.getItemsString())
        #Possible Exits from the room
        print(newPlayer.currentRoom.getExitsString())
        #The player's item if they have any
        print(newPlayer)

        cmd = input(
            """Which way will you go? [n, s, e, w, or q to quit (or i for inventory)]:
            Your options:
            get <itemName>
            drop <itemName>\n 
            """).lower()

        directions = ["n", "s", "e", "w"]
        gets = newPlayer.currentRoom.gets()
        drops = newPlayer.drops()
        print(gets, drops)
        if cmd == "q":
            print("GAME OVER")
            break
        if cmd in directions:
            newPlayer.travel(cmd)
        elif cmd in gets:
            itemIndex = gets.index(cmd)
            newPlayer.addItem(newPlayer.currentRoom.items[itemIndex])
        elif cmd in drops:
            itemIndex = drops.index(cmd)
            newPlayer.removeItem(newPlayer.inventory[itemIndex])
        else:
            print("Incorrect Command!")

        


startAdventure()
