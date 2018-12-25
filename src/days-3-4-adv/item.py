
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f'You pick up the {self.name} and add it to your bag.')
    def on_drop(self):
        print(f'You drop the {self.name}.')
        def print_descr(player):
        if it