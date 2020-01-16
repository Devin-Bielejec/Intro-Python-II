# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, startingRoom):
        self.currentRoom = startingRoom
        self.inventory = []

    def addItem(self, itemName):
        #Check if item is in room to add
        for roomItem in self.currentRoom.items:
            if roomItem.name.lower() == itemName:
                self.inventory.append(roomItem)
                roomItem.on_take()
                self.currentRoom.removeItem(roomItem)
        else:
            print("Not possible yo")

    def removeItem(self, itemName):
        for inventoryItem in self.inventory:
            if inventoryItem.name.lower() == itemName:
                self.inventory.remove(inventoryItem)
                inventoryItem.on_drop()
                self.currentRoom.addItem(inventoryItem)

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
