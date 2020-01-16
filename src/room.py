# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def gets(self):
        return [f"get {item.name.lower()}" for item in self.items]

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def __str__(self):
        displayString = f"\n-------------------\n"
        displayString += f"\n{self.name}\n"
        displayString += f"\n{self.description}\n"
        return displayString

    def getItemsString(self):
        displayString = ""
        if len(self.items) > 0:
            displayString += f"This room has the following items:\n"
            for item in self.items:
                displayString += f"{item.name} ({item.description})\n"
        else:
            displayString += "There are no items in the room."
        return displayString

    def getRoomInDirection(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def getExits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits
  
    def getExitsString(self):
        return f"Exits: {', '.join(self.getExits())}"
