# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = "There is no room this way!"
        self.w_to = "There is no room this way!"
        self.e_to = "There is no room this way!"
        self.s_to = "There is no room this way!"
        self.items = items
        #used to make user input grab the appropriately indexed item
        self.itemsNames = [x.name for x in self.items]

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)