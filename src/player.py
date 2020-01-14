# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room):
        self.room = room
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)
        item.on_take()

    def removeItem(self, item):
        self.inventory.remove(item)
        item.on_drop()
