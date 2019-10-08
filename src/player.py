# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []
        self.inventoryNames = [x.name for x in self.inventory]


    def addItem(self, item):
        self.inventory.append(item)
        item.on_take()

    def removeItem(self, item):
        self.inventory.remove(item)
        item.on_drop()