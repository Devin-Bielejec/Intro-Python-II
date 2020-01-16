# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, startingRoom):
        self.currentRoom = startingRoom
        self.inventory = []

    def drops(self):
        return [f"drop {item.name.lower()}" for item in self.inventory]

    def addItem(self, item):
        self.inventory.append(item)
        item.on_take()
        self.currentRoom.removeItem(item)

    def removeItem(self, item):
        self.inventory.remove(item)
        item.on_drop()
        self.currentRoom.addItem(item)

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
        else:
            print("You cannot move in that direction")

    def __str__(self):
        displayString = ""
        if len(self.inventory) > 0:
            displayString += f"You are holding the following items:\n"
            for item in self.inventory:
                displayString += f"{item.name} ({item.description})\n"
        else:
            displayString += "You don't have any items."
        return displayString
