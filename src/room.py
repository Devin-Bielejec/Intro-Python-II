# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.name}\n{self.description}\n\n"
