# Write a class to hold player information, e.g. what room they are in
# currently.
from settings import Settings

default_settings = {
    'command_entry_design':'> Enter a Command: '
}

Settings = Settings(default_settings)

class Player:
    def __init__(self, name, room, items = {}, settings = Settings):
        self.name = name
        self.room = room
        self.items = items
        self.settings = settings

    def inventory(self):
        print('\nYou are carrying:\n')
        for item in self.items:
            print(item)