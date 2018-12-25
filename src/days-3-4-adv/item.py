
class Item:
    # Constructor
    def __init__(self, name, description):
        self.name = name
        self.description = description
    # Get Item
    def on_take(self):
        print(f'\nYou pick up the {self.name} and add it to your bag.')
    # Drop Item
    def on_drop(self):
        print(f'\nYou drop the {self.name}.')
    # Check Item (In Inventory or Current Room)
    def on_check(self):
            print(f'\nYou inspect the {self.name} and see...\n\n' + self.description + '\n')
