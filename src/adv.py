from room import Room
from player import Player

# Declare all the rooms

room = {
    'Outside Cave Entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'Foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'Grand Overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'Narrow Passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'Treasure Chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
newPlayer = Player("Outside Cave Entrance")

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

end = False
start = True
while end == False:

    if start == True:
        currentRoom = room[newPlayer.room]
        start = False
    print(currentRoom.name)    
    print(currentRoom.description)

    userInput = input("Which way will you go? [n, s, e, w, or q to quit]:\n\n\n\n\n\n\n\n\n")
    
    map = {
        "Outside Cave Entrance": ["n"],
        "Foyer": ["s","n","e"],
        "Grand Overlook": ["s"],
        "Narrow Passage":["w","n"],
        "Treasure Chamber": ["s"]
    }

    if userInput in map[newPlayer.room]:
        print("hi")
        if userInput == "n":
            print(room[currentRoom.name].n_to)
            currentRoom = room[currentRoom.name].n_to
        elif userInput == "s":
            currentRoom = room[currentRoom.name].s_to
        elif userInput == "e":
            currentRoom = room[currentRoom.name].e_to
        elif userInput == "w":
            currentRoom = room[currentRoom.name].w_to
        
        print("Heading to {c}".format(c=currentRoom.name))

    else:
        "You cannot go that way!"

    
    
    if userInput == "q":
        end = True
