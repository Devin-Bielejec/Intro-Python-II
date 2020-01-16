class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        print(f"You have slitherly picked up {self.name}")
    
    def on_drop(self):
        print(f"You have forcefully dropped {self.name}")