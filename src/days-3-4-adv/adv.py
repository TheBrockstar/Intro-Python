from room import Room
from player import Player
from item import Item
import textwrap

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
            input('\nPress Enter to continue...')

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

        ### West
        if caction == 'w' or ((caction == 'go' or caction == 'walk') and (cobject == 'w' or cobject == 'west')):
            if hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
            else:
                nodirection()
            return

        ## - Items
        if caction == 'get':
            if cobject in player.room.items:
                print('You got it!')
            else:
                print('You cannot have it.')
            entocont()


            

    # User Input
    print('__________________________________________________')
    cinput = input('\nEnter a command: => ').split(" ", 1)



    command(cinput)