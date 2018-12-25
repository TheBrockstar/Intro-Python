from room import Room
from player import Player
from item import Item
import textwrap

    # cinput = input('> Enter a Command: ').split(" ", 1) # Plain
    # cinput = input('\n==== Enter a Command ====>>> ').split(" ", 1) # Spear
    # cinput = input('\n>>>>--Enter-a-Command----> ').split(" ", 1) # Arrow
    # cinput = input('\no+++|}=== Enter a Command ====> ').split(" ", 1) # Sword

# System Settings
command_entry_designs = {
    'plain':'> Enter a Command: ',
    'spear':'===== Enter a Command =====>>> ',
    'arrow':'>>>>=---Enter-a-Command-----=> ',
    'sword':'o++++|}==-Enter-a-Command-===> '
}

# Declare all the items
item = {
    'key1': Item("Rusted Iron Key", "A heavy iron key spotted with red blooms of rust.")
}

# Declare all the rooms
room = {
    'outside':  Room("Cave Entrance",
                     "North of you, the cave mouth beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link items to rooms
room['outside'].items = {
        item['key1'].name: item['key1']
    }

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Chosen One", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

cinput = ['begin']
while cinput[0] != 'q':
    # Title
    print('\n--------------------------------------------------')
    print('============== THE CAVERN OF WONDER ==============')
    print('--------------------------------------------------')

    # Location
    print(f'\nYou find yourself at the {player.room.name}. \n')

    ## Location Description
    locationWrapper = textwrap.TextWrapper(50)
    location = locationWrapper.wrap(player.room.description)
    for line in location:
        print(line)
    for item in player.room.items:
        print(player.room.items[item].name)

    # Command Function Container
    def command(command):

        # Define Command Action
        caction = command[0]

        # If One Exists, Define Command Object
        if len(command) == 1:
            cobject = ''
        else:
            cobject = command[1]

        # -- Command Handling

        ## - Helper Functions

        ### Press Enter to continue...
        def entocont():
            input('--\nPress Enter to continue...')

        ## - Help
        if caction == 'h' or caction == 'help':
            print("""Lost, traveler?

Commands are made of two words: an action, and an object.
- The action is what you want to do. 
- The object, which is sometimes optional, is what the action should 
be done to.
    
i.e. search room <= 'search' is the action, and 'room' is the object.
Alternatively, this could be written as 'search' because the object 
is sometimes optional.""")
            entocont()

        ## - Movement
        move_types = ('walk', 'go', 'move', 'travel', 'venture', 'proceed')
        move_dir = {
            'north': ('northward', 'north', 'n'),
            'south': ('southward', 'south', 's'),
            'east': ('eastward', 'east', 'e'),
            'west': ('westward', 'west', 'w'),
        }
        
        ### Movement Error
        def nodirection():
            print('\nYou are unable to see a way to move in that direction!')
            entocont()

        ### North
        if caction == 'n':
            if hasattr(player.room, 'n_to'):
                player.room = player.room.n_to
            else:
                nodirection()
            return
        
        ### South
        if caction == 's':
            if hasattr(player.room, 's_to'):
                player.room = player.room.s_to
            else:
                nodirection()
            return

        ### East
        if caction == 'e':
            if hasattr(player.room, 'e_to'):
                player.room = player.room.e_to
            else:
                nodirection()
            return

        ### West
        if caction == 'w' or (caction in move_types and cobject in move_dir['west']):
            if hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
            else:
                nodirection()
            return

        ## - Items

        ### Get Item
        if caction == 'get' or caction == 'take':
            if cobject in player.room.items:
                player.room.items[cobject].on_take()
                player.items[cobject] = player.room.items[cobject]
                player.room.items.pop(cobject, None)
            else:
                print(f'{cobject} does not exist in this room.')
            entocont()
            return

        ### Drop Item
        if caction == 'drop':
            if cobject in player.items:
                player.items[cobject].on_drop()
                player.room.items[cobject] = player.items[cobject]
                player.items.pop(cobject, None)
            else:
                print(f'{cobject} does not exist in your inventory.')
            entocont()
            return

        ### Check Item
        if caction == 'check':
            if cobject in player.room.items:
                player.room.items[cobject].on_check()
            elif cobject in player.items:
                player.items[cobject].on_check()
            else:
                print(f"An item must be nearby for you to inspect it!")
            entocont()
            return

                
        
        ## - Player Status
        
        ### Check Inventory
        if caction in ('i', 'inventory', 'bag'):
            player.inventory()
            entocont()
            return

        ### Check Status

        ## - Settings
        if caction == 'settings':      
            csettings = input("""
Available Settings: 
1. Command Entry Design

""")
            if (csettings in ('1', '1.', 'Command Entry Design')):
                designs = input("""
Command Entry Designs: 
1. Plain (default)
2. Spear
3. Arrow
4. Sword

""")
                if (designs in ('1','1.', 'Plain')):
                    player.settings.command_entry_design = command_entry_designs['plain']
                elif (designs in ('2','2.', 'Spear')):
                    player.settings.command_entry_design = command_entry_designs['spear']
                elif (designs in ('3','3.', 'Arrow')):
                    player.settings.command_entry_design = command_entry_designs['arrow']
                elif (designs in ('4','4.', 'Sword')):
                    player.settings.command_entry_design = command_entry_designs['sword']
                else:
                    print("Selected design does not exist!")
            else:
                print(f"{csettings} setting not found.")
                

        ### Command Entry Design
 
        

    # User Input
    print('__________________________________________________')
    cinput = input(f'\n{player.settings.command_entry_design}').split(" ", 1)
    

    command(cinput)